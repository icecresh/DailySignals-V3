# Daily Signals V3 — 2026-10-15

As of UTC: 2026-10-15T08:23:27.918525+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21069
Upcoming mapped fixtures: 0
Evaluated cells: 0
Research-qualified candidates: 0

## Research candidates — NOT publication-approved

None

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
Blocking reasons: 18

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
- NO_EVALUATED_MARKETS
- NO_VERIFIED_FIXTURES
- SOURCE_WARNINGS

## Exclusions and warnings

Competition coverage is limited to configured leagues with available historical and fixture sources; not all global football.
Card events are yellow cards only, pending verified settlement rules.
Unmapped fixture names and missing source data are excluded.
Research-qualified is NOT equivalent to publication-authorized.

Configured competitions: 19
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 18, "UNMAPPED_TEAM": 1}
- [EXCLUSION] {"error": "ZERO_ELIGIBLE_FIXTURES", "detail": "Inspect source coverage, prematch status and unmapped teams"}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "E2", "fixture": "Mansfield Town vs Oxford United", "error": "UNMAPPED_TEAM", "unmapped_home": "Mansfield Town", "unmapped_away": "Oxford United"}
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
