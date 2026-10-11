"""Turn a completed V3 research run into an immutable, auditable daily report."""
import argparse, json, hashlib
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument("--report",default="reports/v3/report.json")
p.add_argument("--out",default="reports/v3")
args=p.parse_args()
report=json.loads(Path(args.report).read_text())
dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
day=report["date"]
candidates=report.get("research_qualified",[])
lines=["# Daily Signals V3 — "+day,"",
       "As of UTC: "+report["as_of_utc"],"",
       "**NORMAL SIGNALS: No production-approved signals.**","",
       "Historical matches: "+str(report.get("historical_rows",0)),
       "Upcoming mapped fixtures: "+str(report.get("fixtures_seen",0)),
       "Evaluated cells: "+str(report.get("evaluated_cells",0)),
       "Research-qualified candidates: "+str(len(candidates)),"",
       "## Research candidates — NOT publication-approved",""]
for row in sorted(candidates,key=lambda r:(r["market"],-r["probability"])):
    lines.append("- "+row["fixture"]["display"]+" | "+row["market"]+" | research estimate "+format(row["probability"],".1%")+" | "+", ".join(row["models"]))
if not candidates: lines.append("None")
lines+=["","## Holdout research validation",""]
for market,info in report.get("evaluations",{}).items():
    if info.get("status")=="VALIDATED_RESEARCH":
        v=info["holdout_calibrated"]
        lines.append("- "+market+": holdout N="+str(v["n"])+", Brier="+str(v["brier"])+", selected="+", ".join(info["selected"]))
    else: lines.append("- "+market+": "+info.get("status","UNAVAILABLE"))
lines+=["","## Exclusions and warnings","",
        "Competition coverage is limited to configured leagues with available historical and fixture sources; not all global football.",
        "Card events are yellow cards only, pending verified settlement rules.",
        "Unmapped fixture names and missing source data are excluded.",
        "Research-qualified is NOT equivalent to publication-authorized.",""]
lines.append("Configured competitions: "+str(len(report.get("competitions_configured",[]))))
lines.append("Fixture exclusion counts: "+json.dumps(report.get("fixture_exclusion_counts",{}),sort_keys=True))
for issue in report.get("warnings",[])+report.get("fixture_issues",[]):
    prefix="INFO" if issue.get("severity")=="INFO" else "EXCLUSION"
    lines.append("- ["+prefix+"] "+json.dumps(issue,ensure_ascii=False))
(dest/"NORMAL_SIGNALS.md").write_text("\n".join(lines)+"\n")
(dest/"research_candidates.json").write_text(json.dumps(candidates,indent=2))
digest=hashlib.sha256(Path(args.report).read_bytes()).hexdigest()
(dest/"manifest.json").write_text(json.dumps({"date":day,"report_sha256":digest,
    "publication_authorized":False,"candidate_count":len(candidates),
    "as_of_utc":report["as_of_utc"]},indent=2))
print("Prepared dated research ledger:",day,"candidates:",len(candidates),"sha256:",digest)
