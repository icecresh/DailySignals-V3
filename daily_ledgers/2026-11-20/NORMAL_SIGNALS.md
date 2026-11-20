# Daily Signals V3 — 2026-11-20

As of UTC: 2026-11-20T12:57:14.390879+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21815
Upcoming mapped fixtures: 4
Evaluated cells: 52
Research-qualified candidates: 24

## Research candidates — NOT publication-approved

- Metz vs Boulogne | cards_o15 | research estimate 93.5% | extra_trees, hist_gradient_boosting, catboost
- Hellas Verona vs Cesena | cards_o15 | research estimate 88.0% | extra_trees, hist_gradient_boosting, catboost
- Bayern Munich vs FC Cologne | cards_o15 | research estimate 84.7% | extra_trees, hist_gradient_boosting, catboost
- FC Andorra vs Leganés | cards_o25 | research estimate 95.2% | extra_trees, catboost, xgboost
- Bayern Munich vs FC Cologne | corners_o65 | research estimate 99.9% | logistic, catboost, xgboost
- FC Andorra vs Leganés | corners_o65 | research estimate 84.0% | logistic, catboost, xgboost
- Hellas Verona vs Cesena | corners_o65 | research estimate 84.0% | logistic, catboost, xgboost
- Metz vs Boulogne | corners_o65 | research estimate 81.5% | logistic, catboost, xgboost
- Bayern Munich vs FC Cologne | dc_12 | research estimate 99.9% | catboost, logistic, xgboost
- Hellas Verona vs Cesena | dc_12 | research estimate 72.6% | catboost, logistic, xgboost
- Metz vs Boulogne | dc_12 | research estimate 72.6% | catboost, logistic, xgboost
- Bayern Munich vs FC Cologne | dc_1x | research estimate 97.1% | logistic, catboost, xgboost
- Hellas Verona vs Cesena | dc_1x | research estimate 80.4% | logistic, catboost, xgboost
- Metz vs Boulogne | dc_1x | research estimate 75.1% | logistic, catboost, xgboost
- FC Andorra vs Leganés | dc_1x | research estimate 70.7% | logistic, catboost, xgboost
- Bayern Munich vs FC Cologne | fh_o05 | research estimate 92.2% | extra_trees, xgboost, logistic
- Hellas Verona vs Cesena | fh_o05 | research estimate 71.5% | extra_trees, xgboost, logistic
- Metz vs Boulogne | fh_o05 | research estimate 71.5% | extra_trees, xgboost, logistic
- Bayern Munich vs FC Cologne | ft_o15 | research estimate 99.9% | logistic, catboost, extra_trees
- Hellas Verona vs Cesena | ft_o15 | research estimate 74.7% | logistic, catboost, extra_trees
- Metz vs Boulogne | ft_o15 | research estimate 74.7% | logistic, catboost, extra_trees
- FC Andorra vs Leganés | ft_o15 | research estimate 71.5% | logistic, catboost, extra_trees
- Bayern Munich vs FC Cologne | ft_o25 | research estimate 93.0% | catboost, logistic, extra_trees
- Bayern Munich vs FC Cologne | home_win | research estimate 99.9% | logistic, catboost, lightgbm

## Holdout research validation

- fh_o05: holdout N=3979, Brier=0.20204, selected=extra_trees, xgboost, logistic
- ft_o15: holdout N=3979, Brier=0.17257, selected=logistic, catboost, extra_trees
- ft_o25: holdout N=3979, Brier=0.24516, selected=catboost, logistic, extra_trees
- btts: holdout N=3979, Brier=0.24667, selected=catboost, logistic, xgboost
- home_win: holdout N=3979, Brier=0.232, selected=logistic, catboost, lightgbm
- draw: holdout N=3979, Brier=0.19108, selected=catboost, logistic, xgboost
- away_win: holdout N=3979, Brier=0.19671, selected=logistic, xgboost, catboost
- dc_1x: holdout N=3979, Brier=0.19693, selected=logistic, catboost, xgboost
- dc_x2: holdout N=3979, Brier=0.232, selected=logistic, catboost, lightgbm
- dc_12: holdout N=3979, Brier=0.19106, selected=catboost, logistic, xgboost
- corners_o65: holdout N=3979, Brier=0.13003, selected=logistic, catboost, xgboost
- cards_o15: holdout N=3979, Brier=0.09824, selected=extra_trees, hist_gradient_boosting, catboost
- cards_o25: holdout N=3979, Brier=0.19115, selected=extra_trees, catboost, xgboost

## Independent production audit

Production approval: BLOCKED
Blocking reasons: 15

- FIXTURE_INTEGRITY_ISSUES
- INSUFFICIENT_PROSPECTIVE_OUTCOMES
- MISSING_HIGH_CONFIDENCE_CALIBRATION_away_win
- MISSING_HIGH_CONFIDENCE_CALIBRATION_btts
- MISSING_HIGH_CONFIDENCE_CALIBRATION_cards_o15
- MISSING_HIGH_CONFIDENCE_CALIBRATION_cards_o25
- MISSING_HIGH_CONFIDENCE_CALIBRATION_corners_o65
- MISSING_HIGH_CONFIDENCE_CALIBRATION_dc_12
- MISSING_HIGH_CONFIDENCE_CALIBRATION_dc_1x
- MISSING_HIGH_CONFIDENCE_CALIBRATION_dc_x2
- MISSING_HIGH_CONFIDENCE_CALIBRATION_draw
- MISSING_HIGH_CONFIDENCE_CALIBRATION_fh_o05
- MISSING_HIGH_CONFIDENCE_CALIBRATION_ft_o15
- MISSING_HIGH_CONFIDENCE_CALIBRATION_ft_o25
- MISSING_HIGH_CONFIDENCE_CALIBRATION_home_win

## Exclusions and warnings

Competition coverage is limited to configured leagues with available historical and fixture sources; not all global football.
Card events are yellow cards only, pending verified settlement rules.
Unmapped fixture names and missing source data are excluded.
Research-qualified is NOT equivalent to publication-authorized.

Configured competitions: 19
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 9, "UNMAPPED_TEAM": 11}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "E2", "fixture": "Barnsley vs Sheffield Wednesday", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Sheffield Wednesday"}
- [INFO] {"league": "E3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "D2", "fixture": "Arminia Bielefeld vs 1. FC Magdeburg", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "1. FC Magdeburg"}
- [EXCLUSION] {"league": "D2", "fixture": "SV Darmstadt 98 vs 1. FC Heidenheim 1846", "error": "UNMAPPED_TEAM", "unmapped_home": "SV Darmstadt 98", "unmapped_away": "1. FC Heidenheim 1846"}
- [EXCLUSION] {"league": "SP1", "fixture": "Athletic Club vs Espanyol", "error": "UNMAPPED_TEAM", "unmapped_home": "Athletic Club", "unmapped_away": "Espanyol"}
- [INFO] {"league": "I1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "F1", "fixture": "Troyes vs Le Havre AC", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Le Havre AC"}
- [EXCLUSION] {"league": "F2", "fixture": "Annecy vs Clermont Foot", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Clermont Foot"}
- [EXCLUSION] {"league": "F2", "fixture": "AS Nancy Lorraine vs Dijon FCO", "error": "UNMAPPED_TEAM", "unmapped_home": "AS Nancy Lorraine", "unmapped_away": "Dijon FCO"}
- [EXCLUSION] {"league": "F2", "fixture": "Guingamp vs Rodez Aveyron", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Rodez Aveyron"}
- [EXCLUSION] {"league": "F2", "fixture": "Red Star FC 93 vs Pau", "error": "UNMAPPED_TEAM", "unmapped_home": "Red Star FC 93", "unmapped_away": "Pau"}
- [INFO] {"league": "N1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "B1", "fixture": "Cercle Brugge KSV vs KVC Westerlo", "error": "UNMAPPED_TEAM", "unmapped_home": "Cercle Brugge KSV", "unmapped_away": null}
- [INFO] {"league": "P1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "SC1", "fixture": "Inverness Caledonian Thistle vs Ayr United", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Ayr United"}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
