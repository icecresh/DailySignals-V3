"""Compare research Bayesian estimates with chronological baseline on historical CSVs."""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from daily_signals.history import parse_matches, labels
from daily_signals.bayes import estimate, MARKETS
from daily_signals.validation import metrics
p = argparse.ArgumentParser()
p.add_argument("csv_files", nargs="+")
p.add_argument("--output", default="comparison_report.json")
a = p.parse_args()
rows = []
for f in a.csv_files:
    season, competition = Path(f).stem.split("__", 1)
    rows += parse_matches(Path(f).read_text(encoding="utf-8-sig"), competition, season)
rows.sort(key=lambda r: r["kickoff"])
records, history = [], []
from itertools import groupby
for _, group in groupby(rows, key=lambda r:r["kickoff"]):
    games = list(group)
    for row in games:
        for market in MARKETS:
            actual = labels(row)[market]
            if actual is None: continue
            result = estimate(history, row, market)
            if result["status"] == "UNCALIBRATED":
                records.append({"market": market, "probability": result["p_bayes"], "actual": actual})
    history.extend(games)
report = {"parsed_matches": len(rows), "research_predictions": len(records),
          "metrics": metrics(records), "publication_authorized": False,
          "note": "Uncalibrated research comparison; NOT independent holdout validation."}
Path(a.output).write_text(json.dumps(report, indent=2))
print(json.dumps(report, indent=2))
