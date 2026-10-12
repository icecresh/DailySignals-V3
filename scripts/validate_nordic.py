"""Validate licensed Nordic match CSVs before enabling new leagues.
Usage: python scripts/validate_nordic.py --nor data/nor.csv --den data/den.csv --swe data/swe.csv
Inputs use canonical headers Date,HomeTeam,AwayTeam,FTHG,FTAG,HTHG,HTAG,HC,AC,HY,AY.
No network downloads; do not treat missing statistics as zero.
"""
import argparse, csv, json
from collections import Counter
from datetime import datetime
from pathlib import Path

REQUIRED=("Date","HomeTeam","AwayTeam","FTHG","FTAG","HTHG","HTAG","HC","AC","HY","AY")
NUMERIC=("FTHG","FTAG","HTHG","HTAG","HC","AC","HY","AY")
MIN_MATCHES=600
MIN_SEASONS=3
MIN_COVERAGE=.95

def validate(path):
    with open(path,encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f)
        missing=[x for x in REQUIRED if x not in (reader.fieldnames or [])]
        if missing:return {"pass":False,"reason":"MISSING_COLUMNS","columns":missing}
        rows=list(reader)
    dates=[]; valid=[]; missing_fields=Counter();bad=0;seen=set()
    for r in rows:
        try:
            raw=r["Date"].strip()
            date=None
            for fmt in ("%Y-%m-%d","%d/%m/%Y","%d/%m/%y"):
                try:date=datetime.strptime(raw,fmt).date();break
                except ValueError:pass
            if date is None or not r["HomeTeam"].strip() or not r["AwayTeam"].strip():raise ValueError()
            key=(date.isoformat(),r["HomeTeam"].strip().lower(),r["AwayTeam"].strip().lower())
            if key in seen:raise ValueError()
            seen.add(key)
            dates.append(date)
            parsed={}
            for field in NUMERIC:
                raw=(r.get(field) or "").strip()
                if not raw:missing_fields[field]+=1;parsed[field]=None;continue
                n=float(raw)
                if not n.is_integer() or n<0:raise ValueError()
                parsed[field]=int(n)
            if parsed["FTHG"] is not None and parsed["HTHG"] is not None and parsed["HTHG"]>parsed["FTHG"]:raise ValueError()
            if parsed["FTAG"] is not None and parsed["HTAG"] is not None and parsed["HTAG"]>parsed["FTAG"]:raise ValueError()
            valid.append(parsed)
        except (ValueError,TypeError,KeyError):bad+=1
    n=len(valid)
    seasons=len({d.year for d in dates})
    coverage={f:round(sum(r[f] is not None for r in valid)/n,4) if n else 0 for f in NUMERIC}
    # Every market needs complete outcome labels, including cards/corners.
    passed=(n>=MIN_MATCHES and seasons>=MIN_SEASONS and bad==0 and
            all(v>=MIN_COVERAGE for v in coverage.values()))
    return {"pass":passed,"valid_matches":n,"calendar_years":seasons,"invalid_or_duplicate":bad,
            "field_coverage":coverage,"missing_fields":dict(missing_fields),
            "gates":{"min_matches":MIN_MATCHES,"min_calendar_years":MIN_SEASONS,"min_field_coverage":MIN_COVERAGE},
            "next_gate":"Chronological out-of-time model backtest, fixture identity mapping, and source licence approval"}

def main():
    p=argparse.ArgumentParser()
    for code in ("nor","den","swe"):p.add_argument("--"+code,required=True,type=Path)
    p.add_argument("--out",type=Path)
    a=p.parse_args()
    results={code:validate(getattr(a,code)) for code in ("nor","den","swe")}
    payload={"status":"DATA_QUALITY_VALIDATION_ONLY","leagues":results,
             "all_pass":all(x["pass"] for x in results.values()),
             "note":"Passing does not authorize activation, production predictions or publication."}
    output=json.dumps(payload,indent=2)
    if a.out:a.out.write_text(output+"\n",encoding="utf-8")
    print(output)
    raise SystemExit(0 if payload["all_pass"] else 1)

if __name__=="__main__":main()
