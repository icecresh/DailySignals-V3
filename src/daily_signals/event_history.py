"""Independent Football-Data CSV ingestion. Never use betting odds as features."""
import csv
from io import StringIO
from datetime import datetime

def _count(row, field):
    value = (row.get(field) or "").strip()
    if not value: return None
    try:
        n = int(value)
        return n if n >= 0 else None
    except ValueError: return None

def parse_event_csv(text, competition, season):
    result = []
    for r in csv.DictReader(StringIO(text.lstrip("\ufeff"))):
        home, away = (r.get("HomeTeam") or "").strip(), (r.get("AwayTeam") or "").strip()
        if not home or not away: continue
        try:
            date = datetime.strptime((r.get("Date") or "").strip(), "%d/%m/%Y").date().isoformat()
        except ValueError:
            try: date = datetime.strptime((r.get("Date") or "").strip(), "%d/%m/%y").date().isoformat()
            except ValueError: continue
        hg, ag = _count(r, "FTHG"), _count(r, "FTAG")
        if hg is None or ag is None: continue
        hc, ac = _count(r, "HC"), _count(r, "AC")
        hy, ay = _count(r, "HY"), _count(r, "AY")
        hr, ar = _count(r, "HR"), _count(r, "AR")
        result.append({"date":date,"competition":competition,"season":season,
            "home":home,"away":away,"home_goals":hg,"away_goals":ag,
            "home_ht_goals":_count(r,"HTHG"),"away_ht_goals":_count(r,"HTAG"),
            "corners":None if hc is None or ac is None else hc+ac,
            "yellow_cards":None if hy is None or ay is None else hy+ay,
            "red_cards":None if hr is None or ar is None else hr+ar,
            "referee":(r.get("Referee") or "").strip() or None,
            "source":"football-data.co.uk"})
    return sorted(result, key=lambda x:(x["date"],x["home"],x["away"]))

def event_labels(row):
    corners = row["corners"]
    yellows = row["yellow_cards"]
    # Explicit definition: card markets currently count yellows only.
    # Red-card equivalents are NOT assumed; configure rules before production.
    return {"corners_o65":None if corners is None else int(corners>=7),
            "cards_o15":None if yellows is None else int(yellows>=2),
            "cards_o25":None if yellows is None else int(yellows>=3)}
