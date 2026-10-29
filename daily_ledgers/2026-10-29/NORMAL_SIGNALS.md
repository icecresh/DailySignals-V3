# Daily Signals V3 — 2026-10-29

As of UTC: 2026-10-29T10:57:50.210088+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21413
Upcoming mapped fixtures: 2
Evaluated cells: 26
Research-qualified candidates: 10

## Research candidates — NOT publication-approved

- Frosinone vs Lecce | cards_o15 | research estimate 88.6% | extra_trees, catboost, xgboost
- Fiorentina vs Atalanta | cards_o15 | research estimate 86.8% | extra_trees, catboost, xgboost
- Frosinone vs Lecce | corners_o65 | research estimate 84.6% | logistic, catboost, extra_trees
- Fiorentina vs Atalanta | corners_o65 | research estimate 83.8% | logistic, catboost, extra_trees
- Frosinone vs Lecce | dc_12 | research estimate 74.1% | catboost, logistic, xgboost
- Fiorentina vs Atalanta | dc_12 | research estimate 72.8% | catboost, logistic, xgboost
- Frosinone vs Lecce | dc_1x | research estimate 81.8% | logistic, catboost, xgboost
- Frosinone vs Lecce | fh_o05 | research estimate 70.3% | extra_trees, catboost, logistic
- Frosinone vs Lecce | ft_o15 | research estimate 80.9% | logistic, catboost, xgboost
- Fiorentina vs Atalanta | ft_o15 | research estimate 72.0% | logistic, catboost, xgboost

## Holdout research validation

- fh_o05: holdout N=4067, Brier=0.2022, selected=extra_trees, catboost, logistic
- ft_o15: holdout N=4067, Brier=0.17401, selected=logistic, catboost, xgboost
- ft_o25: holdout N=4067, Brier=0.24517, selected=catboost, logistic, xgboost
- btts: holdout N=4067, Brier=0.24636, selected=catboost, logistic, extra_trees
- home_win: holdout N=4067, Brier=0.23054, selected=catboost, xgboost, logistic
- draw: holdout N=4067, Brier=0.19311, selected=catboost, logistic, xgboost
- away_win: holdout N=4067, Brier=0.19777, selected=logistic, catboost, xgboost
- dc_1x: holdout N=4067, Brier=0.1978, selected=logistic, catboost, xgboost
- dc_x2: holdout N=4067, Brier=0.23055, selected=catboost, xgboost, logistic
- dc_12: holdout N=4067, Brier=0.19314, selected=catboost, logistic, xgboost
- corners_o65: holdout N=4067, Brier=0.13159, selected=logistic, catboost, extra_trees
- cards_o15: holdout N=4067, Brier=0.09814, selected=extra_trees, catboost, xgboost
- cards_o25: holdout N=4067, Brier=0.19174, selected=extra_trees, catboost, hist_gradient_boosting

## Independent production audit

Production approval: BLOCKED
Blocking reasons: 14

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 18}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SP1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SP2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "I2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "F1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "F2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "N1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "B1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "P1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
