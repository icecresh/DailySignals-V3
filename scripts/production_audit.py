"""Independent conservative publication audit; fail closed on missing evidence."""
import math

def audit(report, evaluated):
    issues=[]
    if report.get("publication_authorized") is not False:
        issues.append("INPUT_ALREADY_AUTHORIZED")
    if not report.get("sources"):
        issues.append("NO_HISTORICAL_SOURCES")
    if report.get("warnings"):
        issues.append("SOURCE_WARNINGS")
    fixtures=report.get("fixtures_seen",0)
    if fixtures<1:
        issues.append("NO_VERIFIED_FIXTURES")
    if report.get("fixture_issues"):
        serious=[x for x in report["fixture_issues"] if x.get("severity")!="INFO" and x.get("error")!="NO_SCHEDULED_EVENTS"]
        if serious:issues.append("FIXTURE_INTEGRITY_ISSUES")
    if not evaluated:
        issues.append("NO_EVALUATED_MARKETS")
    seen=set()
    for r in evaluated:
        f=r.get("fixture",{})
        key=(f.get("event_id"),r.get("market"))
        if key in seen:issues.append("DUPLICATE_FIXTURE_MARKET")
        seen.add(key)
        p=r.get("probability")
        if not isinstance(p,(int,float)) or not math.isfinite(p) or not 0<=p<=1:
            issues.append("INVALID_PROBABILITY")
        if not f.get("event_id") or not f.get("kickoff") or not f.get("home") or not f.get("away"):
            issues.append("INCOMPLETE_FIXTURE")
        if len(r.get("models",[]))<2:issues.append("INSUFFICIENT_MODEL_AGREEMENT_EVIDENCE")
    for market,metrics in report.get("evaluations",{}).items():
        if metrics.get("status")!="VALIDATED_RESEARCH":
            issues.append("UNVALIDATED_MARKET_"+market)
            continue
        holdout=metrics.get("holdout_calibrated",{})
        if holdout.get("n",0)<200:issues.append("SMALL_HOLDOUT_"+market)
        # Overall Brier is not enough to prove calibration in the >=70% or >=80% tail.
        if not metrics.get("threshold_bin_validation"):
            issues.append("MISSING_HIGH_CONFIDENCE_CALIBRATION_"+market)
    if not report.get("forward_test_summary",{}).get("sufficient_outcomes"):
        issues.append("INSUFFICIENT_PROSPECTIVE_OUTCOMES")
    # Current pipeline lacks per-model live forecasts, so agreement cannot be audited.
    if not all("model_probabilities" in r for r in evaluated):
        issues.append("MISSING_PER_MODEL_LIVE_PROBABILITIES")
    return {"production_approved":False,"gate":"FAIL_CLOSED",
            "blocking_reasons":sorted(set(issues)),
            "evaluated_cells":len(evaluated),"fixtures_seen":fixtures}
