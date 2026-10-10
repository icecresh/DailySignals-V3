"""Run chronological baseline validation on local footballcsv CSVs."""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from daily_signals.history import parse_matches
from daily_signals.validation import walk_forward, metrics
p = argparse.ArgumentParser()
p.add_argument("csv_files", nargs="+")
p.add_argument("--min-history", type=int, default=100)
p.add_argument("--output", default="validation_report.json")
args = p.parse_args()
rows = []
for f in args.csv_files:
    path = Path(f)
    season, competition = path.stem.split("__", 1)
    rows.extend(parse_matches(path.read_text(encoding="utf-8-sig"), competition, season))
preds = walk_forward(rows, min_history=args.min_history)
report = {"source_files": args.csv_files, "parsed_matches": len(rows),
    "validated_predictions": len(preds), "metrics": metrics(preds),
    "note": "Competition baseline only; NOT a validated Bayesian or V3 signal engine."}
Path(args.output).write_text(json.dumps(report, indent=2))
print(json.dumps(report, indent=2))
