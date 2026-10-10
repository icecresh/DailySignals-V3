"""Leakage-safe expanding-window competition baseline, NOT a V3 predictive model."""
from collections import defaultdict
from itertools import groupby
from math import log
from .history import labels
MARKETS = ("ft_o15", "ft_o25", "btts", "fh_o05")
def walk_forward(rows, min_history=100, prior_strength=40):
    rows = sorted(rows, key=lambda r: (r["kickoff"], r["home"], r["away"]))
    history = defaultdict(list)
    predictions = []
    for kickoff, group in groupby(rows, key=lambda r: r["kickoff"]):
        games = list(group)
        for row in games:
            comp = row["competition"]
            for market, outcome in labels(row).items():
                if market not in MARKETS or outcome is None:
                    continue
                pool, global_pool = history[(comp, market)], history[("*", market)]
                if len(global_pool) < min_history:
                    continue
                prior = (sum(global_pool) + 1) / (len(global_pool) + 2)
                p = (sum(pool) + prior_strength * prior) / (len(pool) + prior_strength)
                predictions.append(dict(kickoff=kickoff, competition=comp, market=market,
                    probability=p, actual=outcome, method="shrunk_competition_baseline"))
        for row in games:
            for market, outcome in labels(row).items():
                if market in MARKETS and outcome is not None:
                    history[(row["competition"], market)].append(outcome)
                    history[("*", market)].append(outcome)
    return predictions
def metrics(predictions):
    by_market = defaultdict(list)
    for p in predictions:
        by_market[p["market"]].append(p)
    result = {}
    for market, ps in by_market.items():
        n = len(ps)
        brier = sum((p["probability"] - p["actual"]) ** 2 for p in ps) / n
        logloss = -sum(p["actual"] * log(max(p["probability"], 1e-12)) +
            (1-p["actual"]) * log(max(1-p["probability"], 1e-12)) for p in ps) / n
        result[market] = dict(n=n, brier=brier, log_loss=logloss,
            observed_rate=sum(p["actual"] for p in ps)/n,
            mean_predicted=sum(p["probability"] for p in ps)/n)
    return result
