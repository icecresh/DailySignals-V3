# Daily Signals V3 — 2026-11-14

As of UTC: 2026-11-14T11:32:10.904314+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21775
Upcoming mapped fixtures: 4
Evaluated cells: 52
Research-qualified candidates: 22

## Research candidates — NOT publication-approved

- AFC Wimbledon vs Blackpool | cards_o15 | research estimate 88.0% | extra_trees, hist_gradient_boosting, catboost
- Mallorca vs Córdoba | cards_o25 | research estimate 93.9% | extra_trees, catboost, xgboost
- Almería vs FC Andorra | cards_o25 | research estimate 89.7% | extra_trees, catboost, xgboost
- Stenhousemuir vs Queen's Park | cards_o25 | research estimate 80.8% | extra_trees, catboost, xgboost
- AFC Wimbledon vs Blackpool | corners_o65 | research estimate 88.2% | logistic, catboost, xgboost
- Almería vs FC Andorra | corners_o65 | research estimate 81.3% | logistic, catboost, xgboost
- Mallorca vs Córdoba | corners_o65 | research estimate 81.3% | logistic, catboost, xgboost
- Stenhousemuir vs Queen's Park | corners_o65 | research estimate 81.3% | logistic, catboost, xgboost
- Almería vs FC Andorra | dc_12 | research estimate 76.4% | catboost, logistic, xgboost
- AFC Wimbledon vs Blackpool | dc_12 | research estimate 72.7% | catboost, logistic, xgboost
- Mallorca vs Córdoba | dc_12 | research estimate 71.8% | catboost, logistic, xgboost
- Stenhousemuir vs Queen's Park | dc_12 | research estimate 71.8% | catboost, logistic, xgboost
- Almería vs FC Andorra | dc_1x | research estimate 81.5% | logistic, xgboost, catboost
- Stenhousemuir vs Queen's Park | dc_1x | research estimate 78.8% | logistic, xgboost, catboost
- AFC Wimbledon vs Blackpool | dc_1x | research estimate 70.4% | logistic, xgboost, catboost
- Mallorca vs Córdoba | dc_1x | research estimate 70.4% | logistic, xgboost, catboost
- AFC Wimbledon vs Blackpool | fh_o05 | research estimate 76.0% | extra_trees, xgboost, logistic
- Almería vs FC Andorra | fh_o05 | research estimate 73.1% | extra_trees, xgboost, logistic
- Almería vs FC Andorra | ft_o15 | research estimate 77.1% | logistic, catboost, xgboost
- AFC Wimbledon vs Blackpool | ft_o15 | research estimate 73.4% | logistic, catboost, xgboost
- Mallorca vs Córdoba | ft_o15 | research estimate 73.4% | logistic, catboost, xgboost
- Stenhousemuir vs Queen's Park | ft_o15 | research estimate 73.4% | logistic, catboost, xgboost

## Holdout research validation

- fh_o05: holdout N=4082, Brier=0.2028, selected=extra_trees, xgboost, logistic
- ft_o15: holdout N=4082, Brier=0.17381, selected=logistic, catboost, xgboost
- ft_o25: holdout N=4082, Brier=0.24554, selected=catboost, logistic, xgboost
- btts: holdout N=4082, Brier=0.24654, selected=catboost, logistic, extra_trees
- home_win: holdout N=4082, Brier=0.23037, selected=catboost, logistic, xgboost
- draw: holdout N=4082, Brier=0.1918, selected=catboost, logistic, hist_gradient_boosting
- away_win: holdout N=4082, Brier=0.19757, selected=logistic, xgboost, catboost
- dc_1x: holdout N=4082, Brier=0.19751, selected=logistic, xgboost, catboost
- dc_x2: holdout N=4082, Brier=0.23036, selected=catboost, logistic, xgboost
- dc_12: holdout N=4082, Brier=0.1917, selected=catboost, logistic, xgboost
- corners_o65: holdout N=4082, Brier=0.13045, selected=logistic, catboost, xgboost
- cards_o15: holdout N=4082, Brier=0.09851, selected=extra_trees, hist_gradient_boosting, catboost
- cards_o25: holdout N=4082, Brier=0.1916, selected=extra_trees, catboost, xgboost

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
Fixture exclusion counts: {"NOT_PREMATCH": 7, "NO_SCHEDULED_EVENTS": 15, "UNMAPPED_TEAM": 20}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "E2", "event_id": "401880753", "error": "NOT_PREMATCH"}
- [EXCLUSION] {"league": "E2", "event_id": "401880752", "error": "NOT_PREMATCH"}
- [EXCLUSION] {"league": "E2", "event_id": "401880751", "error": "NOT_PREMATCH"}
- [EXCLUSION] {"league": "E2", "fixture": "Milton Keynes Dons vs Burton Albion", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Burton Albion"}
- [EXCLUSION] {"league": "E2", "fixture": "Sheffield Wednesday vs Plymouth Argyle", "error": "UNMAPPED_TEAM", "unmapped_home": "Sheffield Wednesday", "unmapped_away": "Plymouth Argyle"}
- [EXCLUSION] {"league": "E2", "event_id": "401880746", "error": "NOT_PREMATCH"}
- [EXCLUSION] {"league": "E2", "fixture": "Stockport County vs Reading", "error": "UNMAPPED_TEAM", "unmapped_home": "Stockport County", "unmapped_away": null}
- [EXCLUSION] {"league": "E2", "fixture": "Wigan Athletic vs Barnsley", "error": "UNMAPPED_TEAM", "unmapped_home": "Wigan Athletic", "unmapped_away": null}
- [EXCLUSION] {"league": "E2", "event_id": "401880743", "error": "NOT_PREMATCH"}
- [EXCLUSION] {"league": "E3", "fixture": "Exeter City vs Cheltenham Town", "error": "UNMAPPED_TEAM", "unmapped_home": "Exeter City", "unmapped_away": "Cheltenham Town"}
- [EXCLUSION] {"league": "E3", "fixture": "Bristol Rovers vs Chesterfield", "error": "UNMAPPED_TEAM", "unmapped_home": "Bristol Rovers", "unmapped_away": null}
- [EXCLUSION] {"league": "E3", "fixture": "Colchester United vs Gillingham", "error": "UNMAPPED_TEAM", "unmapped_home": "Colchester United", "unmapped_away": null}
- [EXCLUSION] {"league": "E3", "fixture": "Crewe Alexandra vs Newport County", "error": "UNMAPPED_TEAM", "unmapped_home": "Crewe Alexandra", "unmapped_away": null}
- [EXCLUSION] {"league": "E3", "fixture": "Port Vale vs Accrington Stanley", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Accrington Stanley"}
- [EXCLUSION] {"league": "E3", "fixture": "Rochdale vs York City", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "York City"}
- [EXCLUSION] {"league": "E3", "event_id": "401881269", "error": "NOT_PREMATCH"}
- [EXCLUSION] {"league": "E3", "fixture": "Salford City vs Northampton Town", "error": "UNMAPPED_TEAM", "unmapped_home": "Salford City", "unmapped_away": "Northampton Town"}
- [EXCLUSION] {"league": "E3", "fixture": "Shrewsbury Town vs Oldham Athletic", "error": "UNMAPPED_TEAM", "unmapped_home": "Shrewsbury Town", "unmapped_away": "Oldham Athletic"}
- [EXCLUSION] {"league": "E3", "fixture": "Swindon Town vs Grimsby Town", "error": "UNMAPPED_TEAM", "unmapped_home": "Swindon Town", "unmapped_away": "Grimsby Town"}
- [EXCLUSION] {"league": "E3", "event_id": "401881265", "error": "NOT_PREMATCH"}
- [EXCLUSION] {"league": "E3", "fixture": "Fleetwood Town vs Tranmere Rovers", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Tranmere Rovers"}
- [INFO] {"league": "D1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SP1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "SP2", "fixture": "Real Valladolid vs Castellón", "error": "UNMAPPED_TEAM", "unmapped_home": "Real Valladolid", "unmapped_away": null}
- [EXCLUSION] {"league": "SP2", "fixture": "Real Sociedad II vs Sporting Gijón", "error": "UNMAPPED_TEAM", "unmapped_home": "Real Sociedad II", "unmapped_away": null}
- [EXCLUSION] {"league": "SP2", "fixture": "Real Oviedo vs Girona", "error": "UNMAPPED_TEAM", "unmapped_home": "Real Oviedo", "unmapped_away": null}
- [INFO] {"league": "I1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "I2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "F1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "F2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "N1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "B1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "P1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "SC1", "fixture": "Ayr United vs Raith Rovers", "error": "UNMAPPED_TEAM", "unmapped_home": "Ayr United", "unmapped_away": "Raith Rovers"}
- [EXCLUSION] {"league": "SC1", "fixture": "Livingston vs Greenock Morton", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Greenock Morton"}
- [EXCLUSION] {"league": "SC1", "fixture": "Partick Thistle vs Inverness Caledonian Thistle", "error": "UNMAPPED_TEAM", "unmapped_home": "Partick Thistle", "unmapped_away": null}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
