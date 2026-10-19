# Daily Signals V3 — 2026-10-19

As of UTC: 2026-10-19T09:00:12.033444+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21069
Upcoming mapped fixtures: 2
Evaluated cells: 26
Research-qualified candidates: 9

## Research candidates — NOT publication-approved

- Monza vs Cagliari | cards_o15 | research estimate 88.0% | extra_trees, hist_gradient_boosting, catboost
- Parma vs Torino | cards_o15 | research estimate 88.0% | extra_trees, hist_gradient_boosting, catboost
- Monza vs Cagliari | corners_o65 | research estimate 81.5% | logistic, catboost, extra_trees
- Parma vs Torino | corners_o65 | research estimate 77.8% | logistic, catboost, extra_trees
- Monza vs Cagliari | dc_12 | research estimate 73.4% | catboost, logistic, xgboost
- Parma vs Torino | dc_12 | research estimate 73.4% | catboost, logistic, xgboost
- Monza vs Cagliari | dc_x2 | research estimate 77.5% | xgboost, catboost, lightgbm
- Monza vs Cagliari | ft_o15 | research estimate 72.1% | logistic, catboost, extra_trees
- Parma vs Torino | ft_o15 | research estimate 72.1% | logistic, catboost, extra_trees

## Holdout research validation

- fh_o05: holdout N=3917, Brier=0.20305, selected=xgboost, catboost, extra_trees
- ft_o15: holdout N=3917, Brier=0.17522, selected=logistic, catboost, extra_trees
- ft_o25: holdout N=3917, Brier=0.24558, selected=catboost, logistic, extra_trees
- btts: holdout N=3917, Brier=0.24667, selected=catboost, logistic, extra_trees
- home_win: holdout N=3917, Brier=0.23131, selected=xgboost, catboost, lightgbm
- draw: holdout N=3917, Brier=0.19402, selected=catboost, logistic, xgboost
- away_win: holdout N=3917, Brier=0.19694, selected=logistic, xgboost, catboost
- dc_1x: holdout N=3917, Brier=0.19693, selected=logistic, xgboost, catboost
- dc_x2: holdout N=3917, Brier=0.23131, selected=xgboost, catboost, lightgbm
- dc_12: holdout N=3917, Brier=0.19402, selected=catboost, logistic, xgboost
- corners_o65: holdout N=3917, Brier=0.1306, selected=logistic, catboost, extra_trees
- cards_o15: holdout N=3917, Brier=0.09646, selected=extra_trees, hist_gradient_boosting, catboost
- cards_o25: holdout N=3917, Brier=0.19059, selected=extra_trees, catboost, hist_gradient_boosting

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 13, "UNMAPPED_TEAM": 5}
- [EXCLUSION] {"league": "E0", "fixture": "Tottenham Hotspur vs Coventry City", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Coventry City"}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "SP1", "fixture": "Getafe vs Rayo Vallecano", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Rayo Vallecano"}
- [EXCLUSION] {"league": "SP2", "fixture": "RC Celta Fortuna vs Tenerife", "error": "UNMAPPED_TEAM", "unmapped_home": "RC Celta Fortuna", "unmapped_away": null}
- [INFO] {"league": "I2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "F1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "F2", "fixture": "Rodez Aveyron vs Montpellier", "error": "UNMAPPED_TEAM", "unmapped_home": "Rodez Aveyron", "unmapped_away": null}
- [INFO] {"league": "N1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "B1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "P1", "fixture": "Braga vs Gil Vicente", "error": "UNMAPPED_TEAM", "unmapped_home": "Braga", "unmapped_away": null}
- [INFO] {"league": "SC0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
