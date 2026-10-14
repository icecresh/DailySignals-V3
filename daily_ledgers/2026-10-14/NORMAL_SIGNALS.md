# Daily Signals V3 — 2026-10-14

As of UTC: 2026-10-14T08:47:53.775017+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21056
Upcoming mapped fixtures: 1
Evaluated cells: 13
Research-qualified candidates: 6

## Research candidates — NOT publication-approved

- Portsmouth vs Sheffield United | cards_o15 | research estimate 87.9% | extra_trees, hist_gradient_boosting, catboost
- Portsmouth vs Sheffield United | corners_o65 | research estimate 86.6% | logistic, catboost, extra_trees
- Portsmouth vs Sheffield United | dc_12 | research estimate 75.5% | catboost, hist_gradient_boosting, logistic
- Portsmouth vs Sheffield United | dc_1x | research estimate 76.8% | xgboost, logistic, catboost
- Portsmouth vs Sheffield United | fh_o05 | research estimate 71.2% | catboost, extra_trees, xgboost
- Portsmouth vs Sheffield United | ft_o15 | research estimate 79.9% | logistic, catboost, extra_trees

## Holdout research validation

- fh_o05: holdout N=3917, Brier=0.20333, selected=catboost, extra_trees, xgboost
- ft_o15: holdout N=3917, Brier=0.17577, selected=logistic, catboost, extra_trees
- ft_o25: holdout N=3917, Brier=0.24528, selected=catboost, logistic, xgboost
- btts: holdout N=3917, Brier=0.24657, selected=extra_trees, catboost, logistic
- home_win: holdout N=3917, Brier=0.23052, selected=catboost, xgboost, logistic
- draw: holdout N=3917, Brier=0.19362, selected=catboost, logistic, extra_trees
- away_win: holdout N=3917, Brier=0.19688, selected=xgboost, logistic, catboost
- dc_1x: holdout N=3917, Brier=0.19687, selected=xgboost, logistic, catboost
- dc_x2: holdout N=3917, Brier=0.23048, selected=catboost, xgboost, logistic
- dc_12: holdout N=3917, Brier=0.19456, selected=catboost, hist_gradient_boosting, logistic
- corners_o65: holdout N=3917, Brier=0.13041, selected=logistic, catboost, extra_trees
- cards_o15: holdout N=3917, Brier=0.09613, selected=extra_trees, hist_gradient_boosting, catboost
- cards_o25: holdout N=3917, Brier=0.19061, selected=extra_trees, catboost, hist_gradient_boosting

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 18, "UNMAPPED_TEAM": 3}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "E1", "fixture": "Norwich City vs Southampton", "error": "UNMAPPED_TEAM", "unmapped_home": "Norwich City", "unmapped_away": null}
- [EXCLUSION] {"league": "E1", "fixture": "Queens Park Rangers vs Derby County", "error": "UNMAPPED_TEAM", "unmapped_home": "Queens Park Rangers", "unmapped_away": "Derby County"}
- [EXCLUSION] {"league": "E1", "fixture": "Lincoln City vs West Ham United", "error": "UNMAPPED_TEAM", "unmapped_home": "Lincoln City", "unmapped_away": null}
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
