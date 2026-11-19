# Daily Signals V3 — 2026-11-19

As of UTC: 2026-11-19T13:10:44.373958+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21815
Upcoming mapped fixtures: 0
Evaluated cells: 0
Research-qualified candidates: 0

## Research candidates — NOT publication-approved

None

## Holdout research validation

- fh_o05: holdout N=3979, Brier=0.20217, selected=extra_trees, xgboost, logistic
- ft_o15: holdout N=3979, Brier=0.17268, selected=logistic, catboost, extra_trees
- ft_o25: holdout N=3979, Brier=0.2451, selected=catboost, logistic, extra_trees
- btts: holdout N=3979, Brier=0.24667, selected=catboost, logistic, xgboost
- home_win: holdout N=3979, Brier=0.23195, selected=logistic, catboost, lightgbm
- draw: holdout N=3979, Brier=0.19109, selected=catboost, logistic, xgboost
- away_win: holdout N=3979, Brier=0.19667, selected=logistic, xgboost, catboost
- dc_1x: holdout N=3979, Brier=0.19694, selected=logistic, catboost, xgboost
- dc_x2: holdout N=3979, Brier=0.23203, selected=logistic, catboost, lightgbm
- dc_12: holdout N=3979, Brier=0.19108, selected=catboost, logistic, xgboost
- corners_o65: holdout N=3979, Brier=0.12999, selected=logistic, catboost, xgboost
- cards_o15: holdout N=3979, Brier=0.09824, selected=extra_trees, hist_gradient_boosting, catboost
- cards_o25: holdout N=3979, Brier=0.19115, selected=extra_trees, catboost, xgboost

## Independent production audit

Production approval: BLOCKED
Blocking reasons: 17

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
- NO_EVALUATED_MARKETS
- NO_VERIFIED_FIXTURES
- SOURCE_WARNINGS

## Exclusions and warnings

Competition coverage is limited to configured leagues with available historical and fixture sources; not all global football.
Card events are yellow cards only, pending verified settlement rules.
Unmapped fixture names and missing source data are excluded.
Research-qualified is NOT equivalent to publication-authorized.

Configured competitions: 19
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 19}
- [EXCLUSION] {"error": "ZERO_ELIGIBLE_FIXTURES", "detail": "Inspect source coverage, prematch status and unmapped teams"}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SP1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SP2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
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
