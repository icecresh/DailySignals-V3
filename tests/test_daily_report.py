import json
import subprocess
import sys
from pathlib import Path

def test_daily_report_generation(tmp_path):
    report={"date":"2026-10-11","as_of_utc":"2026-10-11T04:03:00+00:00",
            "historical_rows":5256,"fixtures_seen":0,"evaluated_cells":0,
            "research_qualified":[],"evaluations":{"ft_o15":{"status":"INSUFFICIENT_HISTORY"}},
            "warnings":[],"fixture_issues":[],"publication_authorized":False}
    source=tmp_path/"report.json"
    source.write_text(json.dumps(report))
    dest=tmp_path/"output"
    script=Path(__file__).resolve().parents[1]/"scripts"/"publish_daily_report.py"
    subprocess.run([sys.executable,str(script),"--report",str(source),"--out",str(dest)],check=True)
    assert "No production-approved signals" in (dest/"NORMAL_SIGNALS.md").read_text()
    manifest=json.loads((dest/"manifest.json").read_text())
    assert manifest["date"]=="2026-10-11"
    assert manifest["publication_authorized"] is False
    assert len(manifest["report_sha256"])==64
