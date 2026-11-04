# Daily Signals V3 — 2026-11-04

As of UTC: 2026-11-04T12:12:58.237765+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21614
Upcoming mapped fixtures: 3
Evaluated cells: 39
Research-qualified candidates: 18

## Research candidates — NOT publication-approved

- Cardiff City vs West Ham United | cards_o15 | research estimate 89.3% | extra_trees, catboost, xgboost
- Wrexham vs Middlesbrough | cards_o15 | research estimate 88.1% | extra_trees, catboost, xgboost
- Bristol City vs Wolverhampton Wanderers | cards_o15 | research estimate 88.1% | extra_trees, catboost, xgboost
- Cardiff City vs West Ham United | corners_o65 | research estimate 88.5% | logistic, catboost, xgboost
- Wrexham vs Middlesbrough | corners_o65 | research estimate 88.4% | logistic, catboost, xgboost
- Bristol City vs Wolverhampton Wanderers | corners_o65 | research estimate 88.4% | logistic, catboost, xgboost
- Cardiff City vs West Ham United | dc_12 | research estimate 79.1% | catboost, xgboost, logistic
- Wrexham vs Middlesbrough | dc_12 | research estimate 74.3% | catboost, xgboost, logistic
- Bristol City vs Wolverhampton Wanderers | dc_12 | research estimate 74.3% | catboost, xgboost, logistic
- Cardiff City vs West Ham United | dc_x2 | research estimate 79.3% | catboost, logistic, xgboost
- Wrexham vs Middlesbrough | dc_x2 | research estimate 79.3% | catboost, logistic, xgboost
- Cardiff City vs West Ham United | fh_o05 | research estimate 79.8% | extra_trees, catboost, xgboost
- Wrexham vs Middlesbrough | fh_o05 | research estimate 75.1% | extra_trees, catboost, xgboost
- Bristol City vs Wolverhampton Wanderers | fh_o05 | research estimate 74.6% | extra_trees, catboost, xgboost
- Cardiff City vs West Ham United | ft_o15 | research estimate 81.8% | logistic, catboost, extra_trees
- Wrexham vs Middlesbrough | ft_o15 | research estimate 81.8% | logistic, catboost, extra_trees
- Bristol City vs Wolverhampton Wanderers | ft_o15 | research estimate 81.8% | logistic, catboost, extra_trees
- Cardiff City vs West Ham United | ft_o25 | research estimate 72.3% | catboost, logistic, xgboost

## Holdout research validation

- fh_o05: holdout N=4091, Brier=0.20156, selected=extra_trees, catboost, xgboost
- ft_o15: holdout N=4091, Brier=0.17235, selected=logistic, catboost, extra_trees
- ft_o25: holdout N=4091, Brier=0.24528, selected=catboost, logistic, xgboost
- btts: holdout N=4091, Brier=0.2462, selected=catboost, logistic, extra_trees
- home_win: holdout N=4091, Brier=0.23142, selected=catboost, logistic, xgboost
- draw: holdout N=4091, Brier=0.19241, selected=catboost, xgboost, logistic
- away_win: holdout N=4091, Brier=0.19684, selected=logistic, xgboost, catboost
- dc_1x: holdout N=4091, Brier=0.19692, selected=logistic, xgboost, catboost
- dc_x2: holdout N=4091, Brier=0.23148, selected=catboost, logistic, xgboost
- dc_12: holdout N=4091, Brier=0.19239, selected=catboost, xgboost, logistic
- corners_o65: holdout N=4091, Brier=0.12979, selected=logistic, catboost, xgboost
- cards_o15: holdout N=4091, Brier=0.09703, selected=extra_trees, catboost, xgboost
- cards_o25: holdout N=4091, Brier=0.19211, selected=catboost, extra_trees, xgboost

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 16, "UNMAPPED_TEAM": 2}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "E2", "fixture": "Oxford United vs Reading", "error": "UNMAPPED_TEAM", "unmapped_home": "Oxford United", "unmapped_away": null}
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
- [EXCLUSION] {"league": "B1", "fixture": "KV Kortrijk vs KV Mechelen", "error": "UNMAPPED_TEAM", "unmapped_home": "KV Kortrijk", "unmapped_away": null}
- [INFO] {"league": "P1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
