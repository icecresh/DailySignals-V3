# Daily Signals V3 — 2026-11-09

As of UTC: 2026-11-09T12:55:30.731811+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21773
Upcoming mapped fixtures: 1
Evaluated cells: 13
Research-qualified candidates: 4

## Research candidates — NOT publication-approved

- Las Palmas vs Eldense | cards_o25 | research estimate 89.7% | extra_trees, catboost, xgboost
- Las Palmas vs Eldense | corners_o65 | research estimate 81.3% | logistic, catboost, xgboost
- Las Palmas vs Eldense | dc_1x | research estimate 70.4% | logistic, xgboost, catboost
- Las Palmas vs Eldense | ft_o15 | research estimate 73.4% | logistic, catboost, xgboost

## Holdout research validation

- fh_o05: holdout N=4080, Brier=0.20268, selected=extra_trees, xgboost, logistic
- ft_o15: holdout N=4080, Brier=0.17375, selected=logistic, catboost, xgboost
- ft_o25: holdout N=4080, Brier=0.24555, selected=catboost, logistic, xgboost
- btts: holdout N=4080, Brier=0.24651, selected=catboost, logistic, extra_trees
- home_win: holdout N=4080, Brier=0.23033, selected=catboost, logistic, xgboost
- draw: holdout N=4080, Brier=0.19177, selected=catboost, logistic, hist_gradient_boosting
- away_win: holdout N=4080, Brier=0.19764, selected=logistic, xgboost, catboost
- dc_1x: holdout N=4080, Brier=0.19758, selected=logistic, xgboost, catboost
- dc_x2: holdout N=4080, Brier=0.23032, selected=catboost, logistic, xgboost
- dc_12: holdout N=4080, Brier=0.19166, selected=catboost, logistic, xgboost
- corners_o65: holdout N=4080, Brier=0.13049, selected=logistic, catboost, xgboost
- cards_o15: holdout N=4080, Brier=0.09856, selected=extra_trees, hist_gradient_boosting, catboost
- cards_o25: holdout N=4080, Brier=0.19169, selected=extra_trees, catboost, xgboost

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 18, "UNMAPPED_TEAM": 1}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SP1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "SP2", "fixture": "CD Sabadell vs Real Sociedad II", "error": "UNMAPPED_TEAM", "unmapped_home": "CD Sabadell", "unmapped_away": "Real Sociedad II"}
- [INFO] {"league": "I1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
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
