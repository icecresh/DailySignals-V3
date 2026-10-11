import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from production_audit import audit

def test_audit_fails_closed_without_prospective_validation():
    report={"publication_authorized":False,"sources":[{"rows":500}],"warnings":[],
            "fixtures_seen":1,"fixture_issues":[],
            "evaluations":{"ft_o25":{"status":"VALIDATED_RESEARCH",
                         "holdout_calibrated":{"n":500}}}}
    rows=[{"fixture":{"event_id":"1","kickoff":"2026-10-12T14:00Z",
                      "home":"A","away":"B"},"market":"ft_o25",
           "probability":0.8,"models":["logistic","poisson"],
           "model_probabilities":{"logistic":0.8,"poisson":0.75}}]
    result=audit(report,rows)
    assert result["production_approved"] is False
    assert "INSUFFICIENT_PROSPECTIVE_OUTCOMES" in result["blocking_reasons"]
    assert "MISSING_HIGH_CONFIDENCE_CALIBRATION_ft_o25" in result["blocking_reasons"]

def test_audit_rejects_missing_fixture_identity():
    result=audit({"publication_authorized":False,"sources":[],"fixtures_seen":1,
                  "evaluations":{}},[{"fixture":{},"market":"ft_o15","probability":1.4}])
    assert "INVALID_PROBABILITY" in result["blocking_reasons"]
    assert "INCOMPLETE_FIXTURE" in result["blocking_reasons"]
