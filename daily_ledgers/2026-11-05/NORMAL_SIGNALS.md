# Daily Signals V3 — 2026-11-05

As of UTC: 2026-11-05T12:25:38.992127+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21631
Upcoming mapped fixtures: 0
Evaluated cells: 0
Research-qualified candidates: 0

## Research candidates — NOT publication-approved

None

## Holdout research validation

- fh_o05: holdout N=4090, Brier=0.20094, selected=extra_trees, catboost, xgboost
- ft_o15: holdout N=4090, Brier=0.17196, selected=logistic, catboost, extra_trees
- ft_o25: holdout N=4090, Brier=0.24482, selected=catboost, logistic, hist_gradient_boosting
- btts: holdout N=4090, Brier=0.24687, selected=logistic, catboost, extra_trees
- home_win: holdout N=4090, Brier=0.23125, selected=catboost, logistic, lightgbm
- draw: holdout N=4090, Brier=0.19244, selected=catboost, xgboost, logistic
- away_win: holdout N=4090, Brier=0.19741, selected=logistic, xgboost, catboost
- dc_1x: holdout N=4090, Brier=0.19746, selected=logistic, xgboost, catboost
- dc_x2: holdout N=4090, Brier=0.23121, selected=catboost, logistic, lightgbm
- dc_12: holdout N=4090, Brier=0.1924, selected=catboost, xgboost, logistic
- corners_o65: holdout N=4090, Brier=0.13, selected=logistic, catboost, xgboost
- cards_o15: holdout N=4090, Brier=0.09842, selected=extra_trees, hist_gradient_boosting, catboost
- cards_o25: holdout N=4090, Brier=0.19233, selected=extra_trees, catboost, hist_gradient_boosting

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
