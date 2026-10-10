"""Candidate algorithms are registered, not claimed as trained or validated."""
MARKETS = {
 "fh_o05":{"floor":0.70,"family":"goals"},
 "ft_o15":{"floor":0.70,"family":"goals"},
 "ft_o25":{"floor":0.70,"family":"goals"},
 "btts":{"floor":0.80,"family":"goals"},
 "result_hda":{"floor":0.70,"family":"result"},
 "double_chance":{"floor":0.70,"family":"result"},
 "corners_o65":{"floor":0.70,"family":"corners"},
 "cards_o15":{"floor":0.70,"family":"cards"},
 "cards_o25":{"floor":0.78,"family":"cards"},
}
CANDIDATES = {
 "goals":("poisson","dixon_coles","bivariate_poisson","negative_binomial",
          "hierarchical_bayes","elo","logistic","random_forest","extra_trees",
          "lightgbm","xgboost","catboost"),
 "result":("score_distribution","elo","logistic","hierarchical_bayes",
           "random_forest","extra_trees","lightgbm","xgboost","catboost"),
 "corners":("poisson","negative_binomial","bayesian_count","random_forest",
            "extra_trees","lightgbm","xgboost","catboost"),
 "cards":("poisson","negative_binomial","bayesian_count","referee_adjusted",
          "random_forest","extra_trees","lightgbm","xgboost","catboost"),
}
def candidate_registry():
    return {market:{"status":"NOT_TRAINED","floor":spec["floor"],
            "algorithms":CANDIDATES[spec["family"]]} for market,spec in MARKETS.items()}
