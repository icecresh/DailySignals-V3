# Daily Signals V3 — 2026-10-21

As of UTC: 2026-10-21T08:39:34.951453+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21223
Upcoming mapped fixtures: 1
Evaluated cells: 13
Research-qualified candidates: 6

## Research candidates — NOT publication-approved

- Reading vs Leyton Orient | cards_o15 | research estimate 88.5% | extra_trees, catboost, xgboost
- Reading vs Leyton Orient | corners_o65 | research estimate 88.9% | logistic, catboost, xgboost
- Reading vs Leyton Orient | dc_12 | research estimate 74.2% | catboost, logistic, xgboost
- Reading vs Leyton Orient | dc_1x | research estimate 76.2% | logistic, xgboost, catboost
- Reading vs Leyton Orient | fh_o05 | research estimate 74.4% | extra_trees, catboost, xgboost
- Reading vs Leyton Orient | ft_o15 | research estimate 81.0% | catboost, logistic, xgboost

## Holdout research validation

- fh_o05: holdout N=3964, Brier=0.20322, selected=extra_trees, catboost, xgboost
- ft_o15: holdout N=3964, Brier=0.17524, selected=catboost, logistic, xgboost
- ft_o25: holdout N=3964, Brier=0.24464, selected=catboost, logistic, xgboost
- btts: holdout N=3964, Brier=0.24691, selected=catboost, logistic, extra_trees
- home_win: holdout N=3964, Brier=0.23035, selected=catboost, extra_trees, xgboost
- draw: holdout N=3964, Brier=0.19316, selected=catboost, logistic, xgboost
- away_win: holdout N=3964, Brier=0.19695, selected=logistic, xgboost, catboost
- dc_1x: holdout N=3964, Brier=0.19688, selected=logistic, xgboost, catboost
- dc_x2: holdout N=3964, Brier=0.23035, selected=catboost, extra_trees, xgboost
- dc_12: holdout N=3964, Brier=0.19318, selected=catboost, logistic, xgboost
- corners_o65: holdout N=3964, Brier=0.13121, selected=logistic, catboost, xgboost
- cards_o15: holdout N=3964, Brier=0.09764, selected=extra_trees, catboost, xgboost
- cards_o25: holdout N=3964, Brier=0.19183, selected=extra_trees, catboost, xgboost

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 17, "UNMAPPED_TEAM": 1}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "SP1", "fixture": "Levante vs Athletic Club", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Athletic Club"}
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
