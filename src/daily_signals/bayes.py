"""Research-only time-decayed Bayesian estimates. Never publish uncalibrated probabilities."""
from datetime import datetime, timezone
from math import exp, log
from .history import labels
MARKETS = ("ft_o15", "ft_o25", "btts", "fh_o05")
def estimate(history, fixture, market, min_comp=30, min_team=8, strength=30, half_life=365):
    if market not in MARKETS:
        return {"status": "UNAVAILABLE", "reason": "UNSUPPORTED_MARKET"}
    t = datetime.fromisoformat(fixture["kickoff"].replace("Z", "+00:00"))
    prior = [r for r in history if datetime.fromisoformat(r["kickoff"].replace("Z", "+00:00")) < t
             and r["competition"] == fixture["competition"] and labels(r)[market] is not None]
    if len(prior) < min_comp:
        return {"status": "UNAVAILABLE", "reason": "INSUFFICIENT_COMPETITION_HISTORY"}
    def w(r):
        age = (t - datetime.fromisoformat(r["kickoff"].replace("Z", "+00:00"))).total_seconds()/86400
        return 2 ** (-age / half_life)
    weight = sum(w(r) for r in prior)
    base = (1 + sum(w(r)*labels(r)[market] for r in prior))/(2 + weight)
    home = [r for r in prior if r["home"] == fixture["home"]]
    away = [r for r in prior if r["away"] == fixture["away"]]
    if min(len(home), len(away)) < min_team:
        return {"status": "UNAVAILABLE", "reason": "INSUFFICIENT_TEAM_HISTORY", "p_base": base}
    def shrunk(pool):
        return (strength*base + sum(w(r)*labels(r)[market] for r in pool))/(strength + sum(w(r) for r in pool))
    return {"status": "UNCALIBRATED", "p_bayes": (shrunk(home)+shrunk(away))/2,
            "p_base": base, "comp_n": len(prior), "home_n": len(home), "away_n": len(away),
            "reason": "REQUIRES_OUT_OF_TIME_CALIBRATION"}
