# Daily Signals V3 — 2026-11-03

As of UTC: 2026-11-03T12:00:40.813236+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21614
Upcoming mapped fixtures: 6
Evaluated cells: 78
Research-qualified candidates: 29

## Research candidates — NOT publication-approved

- Birmingham City vs Millwall | cards_o15 | research estimate 89.3% | extra_trees, catboost, xgboost
- Portsmouth vs Swansea City | cards_o15 | research estimate 88.1% | extra_trees, catboost, xgboost
- Preston North End vs Sheffield United | cards_o15 | research estimate 88.1% | extra_trees, catboost, xgboost
- West Bromwich Albion vs Southampton | cards_o15 | research estimate 88.1% | extra_trees, catboost, xgboost
- Charlton Athletic vs Bolton Wanderers | cards_o15 | research estimate 86.5% | extra_trees, catboost, xgboost
- Blackburn Rovers vs Stoke City | cards_o25 | research estimate 81.2% | catboost, extra_trees, xgboost
- Blackburn Rovers vs Stoke City | corners_o65 | research estimate 88.4% | logistic, catboost, xgboost
- Charlton Athletic vs Bolton Wanderers | corners_o65 | research estimate 88.4% | logistic, catboost, xgboost
- Preston North End vs Sheffield United | corners_o65 | research estimate 88.4% | logistic, catboost, xgboost
- Birmingham City vs Millwall | corners_o65 | research estimate 88.4% | logistic, catboost, xgboost
- West Bromwich Albion vs Southampton | corners_o65 | research estimate 88.4% | logistic, catboost, xgboost
- Portsmouth vs Swansea City | corners_o65 | research estimate 85.6% | logistic, catboost, xgboost
- Portsmouth vs Swansea City | dc_12 | research estimate 74.3% | catboost, xgboost, logistic
- Birmingham City vs Millwall | dc_12 | research estimate 74.3% | catboost, xgboost, logistic
- West Bromwich Albion vs Southampton | dc_12 | research estimate 74.3% | catboost, xgboost, logistic
- Blackburn Rovers vs Stoke City | dc_12 | research estimate 72.3% | catboost, xgboost, logistic
- Charlton Athletic vs Bolton Wanderers | dc_12 | research estimate 72.3% | catboost, xgboost, logistic
- Preston North End vs Sheffield United | dc_12 | research estimate 72.3% | catboost, xgboost, logistic
- Birmingham City vs Millwall | dc_1x | research estimate 75.3% | logistic, xgboost, catboost
- Portsmouth vs Swansea City | dc_1x | research estimate 70.7% | logistic, xgboost, catboost
- Birmingham City vs Millwall | fh_o05 | research estimate 75.1% | extra_trees, catboost, xgboost
- West Bromwich Albion vs Southampton | fh_o05 | research estimate 75.1% | extra_trees, catboost, xgboost
- Blackburn Rovers vs Stoke City | fh_o05 | research estimate 74.6% | extra_trees, catboost, xgboost
- Blackburn Rovers vs Stoke City | ft_o15 | research estimate 81.8% | logistic, catboost, extra_trees
- Birmingham City vs Millwall | ft_o15 | research estimate 81.8% | logistic, catboost, extra_trees
- West Bromwich Albion vs Southampton | ft_o15 | research estimate 81.8% | logistic, catboost, extra_trees
- Portsmouth vs Swansea City | ft_o15 | research estimate 78.3% | logistic, catboost, extra_trees
- Charlton Athletic vs Bolton Wanderers | ft_o15 | research estimate 72.5% | logistic, catboost, extra_trees
- Preston North End vs Sheffield United | ft_o15 | research estimate 72.5% | logistic, catboost, extra_trees

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 16, "UNMAPPED_TEAM": 6}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "E1", "fixture": "Derby County vs Norwich City", "error": "UNMAPPED_TEAM", "unmapped_home": "Derby County", "unmapped_away": "Norwich City"}
- [EXCLUSION] {"league": "E1", "fixture": "Queens Park Rangers vs Burnley", "error": "UNMAPPED_TEAM", "unmapped_home": "Queens Park Rangers", "unmapped_away": null}
- [EXCLUSION] {"league": "E1", "fixture": "Watford vs Lincoln City", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Lincoln City"}
- [EXCLUSION] {"league": "E2", "fixture": "Huddersfield Town vs Luton Town", "error": "UNMAPPED_TEAM", "unmapped_home": "Huddersfield Town", "unmapped_away": "Luton Town"}
- [EXCLUSION] {"league": "E2", "fixture": "Wigan Athletic vs Mansfield Town", "error": "UNMAPPED_TEAM", "unmapped_home": "Wigan Athletic", "unmapped_away": "Mansfield Town"}
- [EXCLUSION] {"league": "E3", "fixture": "Northampton Town vs Oldham Athletic", "error": "UNMAPPED_TEAM", "unmapped_home": "Northampton Town", "unmapped_away": "Oldham Athletic"}
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
