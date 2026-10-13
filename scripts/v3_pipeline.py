"""Daily Signals V3: reproducible multi-model research, out-of-time validation and gated daily forecast.
No bookmaker odds. Never publish unvalidated predictions. Each league is evaluated separately.
"""
import argparse, csv, io, json, math, os, re, sys, urllib.request, unicodedata
from collections import defaultdict, deque
from datetime import datetime, timezone, timedelta
from pathlib import Path
import numpy as np
from scipy.stats import poisson, nbinom
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, HistGradientBoostingClassifier
from sklearn.metrics import brier_score_loss, log_loss
from sklearn.isotonic import IsotonicRegression

MARKETS = {"fh_o05":.70,"ft_o15":.70,"ft_o25":.70,"btts":.80,
           "home_win":.70,"draw":.70,"away_win":.70,
           "dc_1x":.70,"dc_x2":.70,"dc_12":.70,
           "corners_o65":.70,"cards_o15":.70,"cards_o25":.78}
LEAGUES = {"E0":"eng.1","E1":"eng.2","E2":"eng.3","E3":"eng.4","D1":"ger.1","D2":"ger.2","SP1":"esp.1","SP2":"esp.2","I1":"ita.1","I2":"ita.2","F1":"fra.1","F2":"fra.2","N1":"ned.1","B1":"bel.1","P1":"por.1","SC0":"sco.1","SC1":"sco.2","SC2":"sco.3","SC3":"sco.4"}
# Nordic expansion is gated until licensed match-level historical feeds are verified.
# Do not add these to LEAGUES until all six market categories pass coverage tests.
NORDIC_PENDING_VALIDATION = {
    "NOR_ELITESERIEN": {"espn": "nor.1", "name": "Norway Eliteserien"},
    "DEN_SUPERLIGA": {"espn": "den.1", "name": "Denmark Superliga"},
    "SWE_ALLSVENSKAN": {"espn": "swe.1", "name": "Sweden Allsvenskan"},
}
ESPN = dict(LEAGUES)
FEATURES = ("home_gf","home_ga","away_gf","away_ga","home_corners","away_corners",
            "home_cards","away_cards","home_form","away_form","home_games","away_games",
            "league_goals","league_corners","league_cards","home_rest","away_rest")
def download(url):
    req=urllib.request.Request(url,headers={"User-Agent":"DailySignalsV3-Research/1.0"})
    with urllib.request.urlopen(req,timeout=35) as resp: return resp.read().decode("utf-8-sig")
def num(row,key):
    try:
        x=float(row.get(key,""))
        return x if np.isfinite(x) and x>=0 else None
    except (ValueError,TypeError): return None
def read_matches(csv_text,league,season):
    out=[]
    for row in csv.DictReader(io.StringIO(csv_text)):
        h,a=(row.get("HomeTeam") or "").strip(),(row.get("AwayTeam") or "").strip()
        hg,ag=num(row,"FTHG"),num(row,"FTAG")
        if not h or not a or hg is None or ag is None: continue
        raw=(row.get("Date") or "").strip()
        date=None
        for fmt in ("%d/%m/%Y","%d/%m/%y","%Y-%m-%d"):
            try: date=datetime.strptime(raw,fmt).date();break
            except ValueError: pass
        if date is None: continue
        out.append({"date":date.isoformat(),"league":league,"season":season,"home":h,"away":a,
                    "hg":int(hg),"ag":int(ag),"hth":num(row,"HTHG"),"hta":num(row,"HTAG"),
                    "hc":num(row,"HC"),"ac":num(row,"AC"),"hy":num(row,"HY"),"ay":num(row,"AY"),
                    "referee":(row.get("Referee") or "").strip()})
    return out
def labels(r):
    hg,ag=r["hg"],r["ag"]; ht=r["hth"];at=r["hta"]
    co=None if r["hc"] is None or r["ac"] is None else r["hc"]+r["ac"]
    ca=None if r["hy"] is None or r["ay"] is None else r["hy"]+r["ay"]
    return {"fh_o05":None if ht is None or at is None else int(ht+at>=1),
            "ft_o15":int(hg+ag>=2),"ft_o25":int(hg+ag>=3),"btts":int(hg>0 and ag>0),
            "home_win":int(hg>ag),"draw":int(hg==ag),"away_win":int(hg<ag),
            "dc_1x":int(hg>=ag),"dc_x2":int(hg<=ag),"dc_12":int(hg!=ag),
            "corners_o65":None if co is None else int(co>=7),
            "cards_o15":None if ca is None else int(ca>=2),
            "cards_o25":None if ca is None else int(ca>=3)}
def avg(values,default):
    return float(np.mean(values)) if values else float(default)
def team_stats(history,team,cutoff):
    recent=[r for r in history if r["home"]==team or r["away"]==team][-12:]
    gf=[];ga=[];corners=[];cards=[];form=[]
    for r in recent:
        home=r["home"]==team
        g1,g2=(r["hg"],r["ag"]) if home else (r["ag"],r["hg"])
        gf.append(g1);ga.append(g2);form.append(3 if g1>g2 else (1 if g1==g2 else 0))
        v=r["hc"] if home else r["ac"]
        if v is not None: corners.append(v)
        v=r["hy"] if home else r["ay"]
        if v is not None: cards.append(v)
    rest=min(30,(datetime.fromisoformat(cutoff)-datetime.fromisoformat(recent[-1]["date"])).days) if recent else 14
    return [avg(gf,1.4),avg(ga,1.4),avg(corners,5),avg(cards,2),avg(form,1.3),len(recent),max(0,rest)]
def feature(history,home,away,date):
    h=team_stats(history,home,date);a=team_stats(history,away,date)
    league_goals=avg([r["hg"]+r["ag"] for r in history[-150:]],2.8)
    league_corners=avg([r["hc"]+r["ac"] for r in history[-150:] if r["hc"] is not None and r["ac"] is not None],10)
    league_cards=avg([r["hy"]+r["ay"] for r in history[-150:] if r["hy"] is not None and r["ay"] is not None],4)
    return [h[0],h[1],a[0],a[1],h[2],a[2],h[3],a[3],h[4],a[4],h[5],a[5],league_goals,league_corners,league_cards,h[6],a[6]]
def dataset(matches):
    byleague=defaultdict(list)
    for r in matches: byleague[r["league"]].append(r)
    rows=[]
    for league,games in byleague.items():
        games.sort(key=lambda r:(r["date"],r["home"],r["away"]))
        hist=[]
        from itertools import groupby
        for date,group in groupby(games,key=lambda r:r["date"]):
            batch=list(group)
            for r in batch:
                if len(hist)<100: continue
                rows.append({"match":r,"x":feature(hist,r["home"],r["away"],date),"y":labels(r)})
            hist.extend(batch)
    return sorted(rows,key=lambda r:(r["match"]["date"],r["match"]["league"],r["match"]["home"]))
def models():
    m={"logistic":LogisticRegression(max_iter=700),
       "random_forest":RandomForestClassifier(n_estimators=120,min_samples_leaf=9,n_jobs=2,random_state=42),
       "extra_trees":ExtraTreesClassifier(n_estimators=120,min_samples_leaf=9,n_jobs=2,random_state=42),
       "hist_gradient_boosting":HistGradientBoostingClassifier(max_iter=100,l2_regularization=4,min_samples_leaf=25,random_state=42)}
    try:
        from lightgbm import LGBMClassifier
        m["lightgbm"]=LGBMClassifier(n_estimators=110,max_depth=4,learning_rate=.04,min_child_samples=30,verbosity=-1,random_state=42)
    except ImportError: pass
    try:
        from xgboost import XGBClassifier
        m["xgboost"]=XGBClassifier(n_estimators=110,max_depth=3,learning_rate=.04,subsample=.85,n_jobs=2,random_state=42)
    except ImportError: pass
    try:
        from catboost import CatBoostClassifier
        m["catboost"]=CatBoostClassifier(iterations=110,depth=4,learning_rate=.04,verbose=False,thread_count=2,random_seed=42)
    except ImportError: pass
    return m
def analytical(x,market):
    hg=max(.05,(x[0]+x[3])/2);ag=max(.05,(x[2]+x[1])/2)
    lam=hg+ag
    if market=="ft_o15":return 1-poisson.cdf(1,lam)
    if market=="ft_o25":return 1-poisson.cdf(2,lam)
    if market=="fh_o05":return 1-poisson.pmf(0,lam*.46)
    if market=="btts":return (1-math.exp(-hg))*(1-math.exp(-ag))
    if market in ("home_win","draw","away_win","dc_1x","dc_x2","dc_12"):
        ph=sum(poisson.pmf(i,hg)*poisson.cdf(i-1,ag) for i in range(14))
        pd=sum(poisson.pmf(i,hg)*poisson.pmf(i,ag) for i in range(14))
        pa=max(0,1-ph-pd)
        return {"home_win":ph,"draw":pd,"away_win":pa,"dc_1x":ph+pd,"dc_x2":pd+pa,"dc_12":ph+pa}[market]
    if market=="corners_o65":return 1-poisson.cdf(6,max(.1,x[4]+x[5]))
    if market in ("cards_o15","cards_o25"):
        return 1-poisson.cdf(1 if market=="cards_o15" else 2,max(.1,x[6]+x[7]))
    raise ValueError(market)
def score(y,p):
    p=np.clip(p,.001,.999)
    return {"n":len(y),"brier":round(float(brier_score_loss(y,p)),5),
            "log_loss":round(float(log_loss(y,p,labels=[0,1])),5),
            "observed":round(float(np.mean(y)),5),"predicted":round(float(np.mean(p)),5)}
def fit_models(train,cal,test,market):
    def eligible(rows):return [r for r in rows if r["y"][market] is not None]
    tr,ca,te=map(eligible,(train,cal,test))
    if len(tr)<250 or len(ca)<80 or len(te)<80:return {"status":"INSUFFICIENT_HISTORY","sizes":[len(tr),len(ca),len(te)]},None
    xtr=np.array([r["x"] for r in tr]);ytr=np.array([r["y"][market] for r in tr])
    xca=np.array([r["x"] for r in ca]);yca=np.array([r["y"][market] for r in ca])
    xte=np.array([r["x"] for r in te]);yte=np.array([r["y"][market] for r in te])
    if len(set(ytr))<2 or len(set(yca))<2 or len(set(yte))<2:return {"status":"ONE_CLASS"},None
    candidate={"poisson":(np.array([analytical(x,market) for x in xca]),np.array([analytical(x,market) for x in xte]),None)}
    fitted={}
    for name,model in models().items():
        try:
            model.fit(xtr,ytr)
            candidate[name]=(model.predict_proba(xca)[:,1],model.predict_proba(xte)[:,1],model)
            fitted[name]=model
        except Exception as exc: print("MODEL_UNAVAILABLE",market,name,str(exc),file=sys.stderr)
    ranking=sorted(candidate,key=lambda n:score(yca,candidate[n][0])["brier"])
    selected=ranking[:min(3,len(ranking))]
    cal_raw=np.mean([candidate[n][0] for n in selected],axis=0)
    test_raw=np.mean([candidate[n][1] for n in selected],axis=0)
    calibrator=IsotonicRegression(y_min=.001,y_max=.999,out_of_bounds="clip")
    calibrator.fit(cal_raw,yca)
    test_cal=calibrator.predict(test_raw)
    result={"status":"VALIDATED_RESEARCH","sizes":{"train":len(tr),"calibration":len(ca),"holdout":len(te)},
            "candidate_calibration_brier":{n:score(yca,candidate[n][0])["brier"] for n in ranking},
            "selected":selected,"holdout_raw":score(yte,test_raw),"holdout_calibrated":score(yte,test_cal),
            "calibration": "isotonic trained only on chronological calibration slice"}
    return result,{"selected":selected,"models":fitted,"calibrator":calibrator,"market":market}
def normal(s):
    ascii_name=unicodedata.normalize("NFKD",s.lower().replace("&","and")).encode("ascii","ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]","",ascii_name)
ALIASES={"manchester united":"man utd","manchester city":"man city","tottenham hotspur":"tottenham",
         "wolverhampton wanderers":"wolves","newcastle united":"newcastle","nottingham forest":"nott'm forest",
         "brighton and hove albion":"brighton","west ham united":"west ham","bayern munich":"bayern munich",
         "paris saint germain":"paris sg","internazionale":"inter"}
TEAM_NAME_VARIANTS = {
    "fc cologne": "FC Koln",
    "borussia monchengladbach": "M'gladbach",
    "sc freiburg": "Freiburg",
    "hertha berlin": "Hertha",
    "spvgg greuther furth": "Greuther Furth",
    "karlsruher sc": "Karlsruhe",
    "vfl bochum": "Bochum",
    "arminia bielefeld": "Bielefeld",
    "celta vigo": "Celta",
    "real sociedad": "Sociedad",
    "real betis": "Betis",
    "racing santander": "Santander",
    "fc andorra": "Andorra",
    "sporting gijon": "Sp Gijon",
    "as roma": "Roma",
    "ac milan": "Milan",
    "hellas verona": "Verona",
    "stade rennais": "Rennes",
    "aj auxerre": "Auxerre",
    "fc utrecht": "Utrecht",
    "pec zwolle": "Zwolle",
    "sc cambuur": "Cambuur",
    "ado den haag": "Den Haag",
    "fc groningen": "Groningen",
    "standard liege": "Standard",
    "royal charleroi sc": "Charleroi",
    "union st gilloise": "St Gilloise",
    "oh leuven": "Oud-Heverlee Leuven",
    "kvc westerlo": "Westerlo",
    "kv mechelen": "Mechelen",
    "sint truidense": "St Truiden",
    "cd nacional": "Nacional",
    "vitoria de guimaraes": "Guimaraes",
    "blackburn rovers": "Blackburn",
    "charlton athletic": "Charlton",
    "cardiff city": "Cardiff",
    "swansea city": "Swansea",
    "bolton wanderers": "Bolton",
    "west bromwich albion": "West Brom",
    "birmingham city": "Birmingham",
    "preston north end": "Preston",
    "stoke city": "Stoke",
    "inverness caledonian thistle": "Inverness C"
}
def resolve(name,teams):
    exact={normal(t):t for t in teams}
    keys=[normal(name)]
    if name.lower() in ALIASES:keys.insert(0,normal(ALIASES[name.lower()]))
    found=[exact[k] for k in keys if k in exact]
    if found: return found[0]
    alt = next((v for k,v in TEAM_NAME_VARIANTS.items() if normal(k)==normal(name)),None)
    if alt and normal(alt) in exact: return exact[normal(alt)]
    # Never fuzzy-match clubs: historical identity must be exact or explicitly mapped.
    return None
def fixtures(day,leagues,history):
    result=[];issues=[]
    for league in leagues:
        url="https://site.api.espn.com/apis/site/v2/sports/soccer/"+ESPN[league]+"/scoreboard?dates="+day.replace("-","")
        try: data=json.loads(download(url))
        except Exception as exc:issues.append({"league":league,"error":str(exc)});continue
        teams=set(r["home"] for r in history if r["league"]==league)|set(r["away"] for r in history if r["league"]==league)
        events=data.get("events",[])
        if not events: issues.append({"league":league,"error":"NO_SCHEDULED_EVENTS","severity":"INFO"})
        for ev in events:
            comps=ev.get("competitions",[])
            if not comps:continue
            competitors=comps[0].get("competitors",[])
            home=next((c for c in competitors if c.get("homeAway")=="home"),None)
            away=next((c for c in competitors if c.get("homeAway")=="away"),None)
            if not home or not away:continue
            if ev.get("status",{}).get("type",{}).get("state")!="pre":
                issues.append({"league":league,"event_id":ev.get("id"),"error":"NOT_PREMATCH"})
                continue
            hn=home["team"].get("displayName","");an=away["team"].get("displayName","")
            h=resolve(hn,teams);a=resolve(an,teams)
            if not h or not a:issues.append({"league":league,"fixture":hn+" vs "+an,"error":"UNMAPPED_TEAM","unmapped_home":hn if not h else None,"unmapped_away":an if not a else None});continue
            # Exclude clubs with no league-specific match history rather than silently using priors.
            if not any(r["home"]==h or r["away"]==h for r in history if r["league"]==league) or not any(r["home"]==a or r["away"]==a for r in history if r["league"]==league):
                issues.append({"league":league,"fixture":hn+" vs "+an,"error":"INSUFFICIENT_TEAM_HISTORY"})
                continue
            result.append({"league":league,"home":h,"away":a,"display":hn+" vs "+an,"kickoff":ev.get("date"),"event_id":ev.get("id")})
    return result,issues
def run(args):
    day=args.date or datetime.now(timezone.utc).date().isoformat()
    seasons=args.seasons.split(",")
    history=[];sources=[];warnings=[]
    for league in LEAGUES:
        for season in seasons:
            yy=season.split("-")[0][-2:]+season.split("-")[1][-2:]
            url="https://www.football-data.co.uk/mmz4281/"+yy+"/"+league+".csv"
            try:
                rows=read_matches(download(url),league,season)
                if len(rows)<100 and season != seasons[-1]: warnings.append({"source":url,"error":"LOW_COVERAGE","rows":len(rows)})
                history+=rows;sources.append({"url":url,"rows":len(rows)})
            except Exception as exc:warnings.append({"source":url,"error":str(exc)})
    history=[r for r in history if r["date"]<day]
    rows=dataset(history)
    # Global date split prevents later league fixtures leaking into earlier training dates.
    dates=sorted(set(r["match"]["date"] for r in rows))
    if len(dates)<60: raise RuntimeError("Insufficient chronological dates for independent validation")
    d1=dates[int(len(dates)*.60)];d2=dates[int(len(dates)*.80)]
    train=[r for r in rows if r["match"]["date"]<d1]
    cal=[r for r in rows if d1<=r["match"]["date"]<d2]
    test=[r for r in rows if r["match"]["date"]>=d2]
    evaluations={};trained={}
    for market in MARKETS:
        evaluations[market],trained[market]=fit_models(train,cal,test,market)
    live,fixture_issues=fixtures(day,LEAGUES,history)
    if not live:
        warnings.append({"error":"ZERO_ELIGIBLE_FIXTURES","detail":"Inspect source coverage, prematch status and unmapped teams"})
    signals=[];evaluated=[]
    for f in live:
        prior=[r for r in history if r["league"]==f["league"] and r["date"]<day]
        if len(prior)<100:continue
        x=feature(prior,f["home"],f["away"],day)
        for market,floor in MARKETS.items():
            fit=trained.get(market)
            if not fit:continue
            probs=[]
            for name in fit["selected"]:
                if name=="poisson":probs.append(analytical(x,market))
                elif name in fit["models"]:probs.append(float(fit["models"][name].predict_proba(np.array([x]))[0,1]))
            if not probs:continue
            p=float(fit["calibrator"].predict([np.mean(probs)])[0])
            disagreement=float(max(probs)-min(probs))
            # Holdout quality gates.  No publish on degraded calibration or weak coverage.
            report=evaluations[market]
            good=(report["holdout_calibrated"]["n"]>=80 and
                  report["holdout_calibrated"]["brier"]<=report["holdout_raw"]["brier"]+.015)
            row={"fixture":f,"market":market,"probability":round(p,4),
                 "models":fit["selected"],"model_probabilities":{name:round(float(v),4) for name,v in zip(fit["selected"],probs)},
                 "model_disagreement":round(disagreement,4),"holdout_brier":report["holdout_calibrated"]["brier"],
                 "status":"QUALIFIED" if p>=floor and good and disagreement<=.20 else "REJECTED"}
            evaluated.append(row)
            if row["status"]=="QUALIFIED":signals.append(row)
    # One card line per fixture; O2.5 takes precedence only if it qualifies.
    by_fixture=defaultdict(list)
    for s in signals:by_fixture[s["fixture"]["event_id"]].append(s)
    signals=[]
    for group in by_fixture.values():
        cards=[s for s in group if s["market"] in ("cards_o15","cards_o25")]
        signals.extend(s for s in group if s not in cards)
        if cards:signals.append(next((s for s in cards if s["market"]=="cards_o25"),cards[0]))
    report={"date":day,"as_of_utc":datetime.now(timezone.utc).isoformat(),
            "status":"RESEARCH_ONLY_NOT_PRODUCTION_AUTHORIZED",
            "sources":sources,"warnings":warnings,"historical_rows":len(history),
            "feature_rows":len(rows),"split_dates":{"calibration_start":d1,"holdout_start":d2},
            "evaluations":evaluations,"fixtures_seen":len(live),"fixture_issues":fixture_issues,
            "competitions_configured":list(LEAGUES),
            "fixture_exclusion_counts":{reason:sum(i.get("error")==reason for i in fixture_issues) for reason in sorted({i.get("error") for i in fixture_issues})},
            "evaluated_cells":len(evaluated),"research_qualified":signals,
            "publication_authorized":False,
            "notes":["Models calibrated on a middle time slice, tested on a later holdout.",
                     "Models are research candidates, not independently approved for publication.",
                     "Cards are yellow cards only; verify settlement conventions.",
                     "Only verified ESPN pre-match fixtures with exact mapped teams evaluated.",
                     "No historical odds used."]}
    dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    (dest/"report.json").write_text(json.dumps(report,indent=2,default=str))
    (dest/"evaluated_cells.json").write_text(json.dumps(evaluated,indent=2,default=str))
    print(json.dumps({"date":day,"historical":len(history),"fixtures":len(live),
                      "evaluated":len(evaluated),"research_qualified":len(signals),
                      "markets_validated":sum(e["status"]=="VALIDATED_RESEARCH" for e in evaluations.values()),
                      "warnings":len(warnings)+len(fixture_issues),
                      "publication_authorized":False},indent=2))
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--date")
    parser.add_argument("--seasons",default="2023-24,2024-25,2025-26,2026-27")
    parser.add_argument("--out",default="reports/v3")
    run(parser.parse_args())
