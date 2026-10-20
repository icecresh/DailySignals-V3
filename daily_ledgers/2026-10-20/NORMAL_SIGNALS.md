# Daily Signals V3 — 2026-10-20

As of UTC: 2026-10-20T08:37:48.874320+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21069
Upcoming mapped fixtures: 3
Evaluated cells: 39
Research-qualified candidates: 17

## Research candidates — NOT publication-approved

- Wolverhampton Wanderers vs Portsmouth | cards_o15 | research estimate 88.0% | extra_trees, hist_gradient_boosting, catboost
- Blackpool vs Milton Keynes Dons | cards_o15 | research estimate 88.0% | extra_trees, hist_gradient_boosting, catboost
- Gillingham vs Port Vale | cards_o15 | research estimate 88.0% | extra_trees, hist_gradient_boosting, catboost
- Wolverhampton Wanderers vs Portsmouth | corners_o65 | research estimate 88.2% | logistic, catboost, extra_trees
- Blackpool vs Milton Keynes Dons | corners_o65 | research estimate 88.1% | logistic, catboost, extra_trees
- Gillingham vs Port Vale | corners_o65 | research estimate 81.5% | logistic, catboost, extra_trees
- Wolverhampton Wanderers vs Portsmouth | dc_12 | research estimate 77.2% | catboost, logistic, xgboost
- Blackpool vs Milton Keynes Dons | dc_12 | research estimate 77.2% | catboost, logistic, xgboost
- Gillingham vs Port Vale | dc_12 | research estimate 73.4% | catboost, logistic, xgboost
- Blackpool vs Milton Keynes Dons | dc_1x | research estimate 79.2% | logistic, xgboost, catboost
- Wolverhampton Wanderers vs Portsmouth | dc_1x | research estimate 77.2% | logistic, xgboost, catboost
- Gillingham vs Port Vale | dc_1x | research estimate 70.1% | logistic, xgboost, catboost
- Wolverhampton Wanderers vs Portsmouth | fh_o05 | research estimate 75.8% | xgboost, catboost, extra_trees
- Blackpool vs Milton Keynes Dons | fh_o05 | research estimate 75.8% | xgboost, catboost, extra_trees
- Wolverhampton Wanderers vs Portsmouth | ft_o15 | research estimate 81.6% | logistic, catboost, extra_trees
- Blackpool vs Milton Keynes Dons | ft_o15 | research estimate 79.3% | logistic, catboost, extra_trees
- Gillingham vs Port Vale | ft_o15 | research estimate 72.1% | logistic, catboost, extra_trees

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 15, "UNMAPPED_TEAM": 22}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "E2", "fixture": "AFC Wimbledon vs Mansfield Town", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Mansfield Town"}
- [EXCLUSION] {"league": "E2", "fixture": "Bromley vs Leicester City", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Leicester City"}
- [EXCLUSION] {"league": "E2", "fixture": "Burton Albion vs Bradford City", "error": "UNMAPPED_TEAM", "unmapped_home": "Burton Albion", "unmapped_away": "Bradford City"}
- [EXCLUSION] {"league": "E2", "fixture": "Cambridge United vs Wycombe Wanderers", "error": "UNMAPPED_TEAM", "unmapped_home": "Cambridge United", "unmapped_away": "Wycombe Wanderers"}
- [EXCLUSION] {"league": "E2", "fixture": "Doncaster Rovers vs Stockport County", "error": "UNMAPPED_TEAM", "unmapped_home": "Doncaster Rovers", "unmapped_away": "Stockport County"}
- [EXCLUSION] {"league": "E2", "fixture": "Huddersfield Town vs Peterborough United", "error": "UNMAPPED_TEAM", "unmapped_home": "Huddersfield Town", "unmapped_away": "Peterborough United"}
- [EXCLUSION] {"league": "E2", "fixture": "Luton Town vs Barnsley", "error": "UNMAPPED_TEAM", "unmapped_home": "Luton Town", "unmapped_away": null}
- [EXCLUSION] {"league": "E2", "fixture": "Notts County vs Sheffield Wednesday", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Sheffield Wednesday"}
- [EXCLUSION] {"league": "E2", "fixture": "Oxford United vs Wigan Athletic", "error": "UNMAPPED_TEAM", "unmapped_home": "Oxford United", "unmapped_away": "Wigan Athletic"}
- [EXCLUSION] {"league": "E2", "fixture": "Stevenage vs Plymouth Argyle", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Plymouth Argyle"}
- [EXCLUSION] {"league": "E3", "fixture": "Barnet vs Swindon Town", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Swindon Town"}
- [EXCLUSION] {"league": "E3", "fixture": "Bristol Rovers vs Salford City", "error": "UNMAPPED_TEAM", "unmapped_home": "Bristol Rovers", "unmapped_away": "Salford City"}
- [EXCLUSION] {"league": "E3", "fixture": "Cheltenham Town vs Fleetwood Town", "error": "UNMAPPED_TEAM", "unmapped_home": "Cheltenham Town", "unmapped_away": null}
- [EXCLUSION] {"league": "E3", "fixture": "Chesterfield vs Colchester United", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Colchester United"}
- [EXCLUSION] {"league": "E3", "fixture": "Crawley Town vs Shrewsbury Town", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Shrewsbury Town"}
- [EXCLUSION] {"league": "E3", "fixture": "Exeter City vs Crewe Alexandra", "error": "UNMAPPED_TEAM", "unmapped_home": "Exeter City", "unmapped_away": "Crewe Alexandra"}
- [EXCLUSION] {"league": "E3", "fixture": "Northampton Town vs Tranmere Rovers", "error": "UNMAPPED_TEAM", "unmapped_home": "Northampton Town", "unmapped_away": "Tranmere Rovers"}
- [EXCLUSION] {"league": "E3", "fixture": "Rochdale vs Grimsby Town", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Grimsby Town"}
- [EXCLUSION] {"league": "E3", "fixture": "Rotherham United vs Newport County", "error": "UNMAPPED_TEAM", "unmapped_home": "Rotherham United", "unmapped_away": null}
- [EXCLUSION] {"league": "E3", "fixture": "Walsall vs Oldham Athletic", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Oldham Athletic"}
- [EXCLUSION] {"league": "E3", "fixture": "York City vs Accrington Stanley", "error": "UNMAPPED_TEAM", "unmapped_home": "York City", "unmapped_away": "Accrington Stanley"}
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
- [EXCLUSION] {"league": "SC1", "fixture": "Dunfermline Athletic vs Partick Thistle", "error": "UNMAPPED_TEAM", "unmapped_home": "Dunfermline Athletic", "unmapped_away": "Partick Thistle"}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
