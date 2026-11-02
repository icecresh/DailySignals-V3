# Daily Signals V3 — 2026-11-02

As of UTC: 2026-11-02T12:29:40.287826+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21602
Upcoming mapped fixtures: 8
Evaluated cells: 104
Research-qualified candidates: 42

## Research candidates — NOT publication-approved

- Sassuolo vs Fiorentina | cards_o15 | research estimate 87.3% | extra_trees, hist_gradient_boosting, catboost
- Atalanta vs Parma | cards_o15 | research estimate 87.3% | extra_trees, hist_gradient_boosting, catboost
- Lorient vs Brest | cards_o15 | research estimate 87.3% | extra_trees, hist_gradient_boosting, catboost
- Benfica vs Alverca | cards_o15 | research estimate 87.3% | extra_trees, hist_gradient_boosting, catboost
- Tenerife vs FC Andorra | cards_o25 | research estimate 89.5% | extra_trees, catboost, xgboost
- Mallorca vs Cádiz | cards_o25 | research estimate 89.5% | extra_trees, catboost, xgboost
- Gil Vicente vs Vitória de Guimaraes | cards_o25 | research estimate 86.6% | extra_trees, catboost, xgboost
- Newcastle United vs Everton | cards_o25 | research estimate 80.3% | extra_trees, catboost, xgboost
- Benfica vs Alverca | corners_o65 | research estimate 87.4% | logistic, catboost, xgboost
- Sassuolo vs Fiorentina | corners_o65 | research estimate 86.0% | logistic, catboost, xgboost
- Newcastle United vs Everton | corners_o65 | research estimate 82.9% | logistic, catboost, xgboost
- Atalanta vs Parma | corners_o65 | research estimate 82.9% | logistic, catboost, xgboost
- Lorient vs Brest | corners_o65 | research estimate 82.9% | logistic, catboost, xgboost
- Tenerife vs FC Andorra | corners_o65 | research estimate 81.1% | logistic, catboost, xgboost
- Gil Vicente vs Vitória de Guimaraes | corners_o65 | research estimate 81.1% | logistic, catboost, xgboost
- Mallorca vs Cádiz | corners_o65 | research estimate 76.2% | logistic, catboost, xgboost
- Benfica vs Alverca | dc_12 | research estimate 86.1% | catboost, xgboost, logistic
- Atalanta vs Parma | dc_12 | research estimate 73.5% | catboost, xgboost, logistic
- Newcastle United vs Everton | dc_12 | research estimate 72.9% | catboost, xgboost, logistic
- Sassuolo vs Fiorentina | dc_12 | research estimate 72.9% | catboost, xgboost, logistic
- Lorient vs Brest | dc_12 | research estimate 72.9% | catboost, xgboost, logistic
- Gil Vicente vs Vitória de Guimaraes | dc_12 | research estimate 72.9% | catboost, xgboost, logistic
- Benfica vs Alverca | dc_1x | research estimate 96.4% | logistic, xgboost, catboost
- Mallorca vs Cádiz | dc_1x | research estimate 81.2% | logistic, xgboost, catboost
- Atalanta vs Parma | dc_1x | research estimate 77.4% | logistic, xgboost, catboost
- Newcastle United vs Everton | dc_1x | research estimate 75.0% | logistic, xgboost, catboost
- Tenerife vs FC Andorra | dc_1x | research estimate 75.0% | logistic, xgboost, catboost
- Lorient vs Brest | dc_1x | research estimate 70.4% | logistic, xgboost, catboost
- Benfica vs Alverca | fh_o05 | research estimate 76.1% | catboost, xgboost, logistic
- Newcastle United vs Everton | fh_o05 | research estimate 71.6% | catboost, xgboost, logistic
- Sassuolo vs Fiorentina | fh_o05 | research estimate 71.6% | catboost, xgboost, logistic
- Atalanta vs Parma | fh_o05 | research estimate 70.7% | catboost, xgboost, logistic
- Lorient vs Brest | fh_o05 | research estimate 70.7% | catboost, xgboost, logistic
- Benfica vs Alverca | ft_o15 | research estimate 82.2% | logistic, catboost, extra_trees
- Sassuolo vs Fiorentina | ft_o15 | research estimate 77.0% | logistic, catboost, extra_trees
- Newcastle United vs Everton | ft_o15 | research estimate 76.8% | logistic, catboost, extra_trees
- Lorient vs Brest | ft_o15 | research estimate 76.8% | logistic, catboost, extra_trees
- Atalanta vs Parma | ft_o15 | research estimate 75.2% | logistic, catboost, extra_trees
- Tenerife vs FC Andorra | ft_o15 | research estimate 72.0% | logistic, catboost, extra_trees
- Mallorca vs Cádiz | ft_o15 | research estimate 72.0% | logistic, catboost, extra_trees
- Benfica vs Alverca | ft_o25 | research estimate 70.9% | catboost, logistic, xgboost
- Benfica vs Alverca | home_win | research estimate 83.3% | logistic, catboost, xgboost

## Holdout research validation

- fh_o05: holdout N=4084, Brier=0.20129, selected=catboost, xgboost, logistic
- ft_o15: holdout N=4084, Brier=0.17204, selected=logistic, catboost, extra_trees
- ft_o25: holdout N=4084, Brier=0.24435, selected=catboost, logistic, xgboost
- btts: holdout N=4084, Brier=0.24616, selected=catboost, logistic, extra_trees
- home_win: holdout N=4084, Brier=0.23122, selected=logistic, catboost, xgboost
- draw: holdout N=4084, Brier=0.19279, selected=catboost, xgboost, logistic
- away_win: holdout N=4084, Brier=0.19667, selected=logistic, xgboost, catboost
- dc_1x: holdout N=4084, Brier=0.19667, selected=logistic, xgboost, catboost
- dc_x2: holdout N=4084, Brier=0.23117, selected=logistic, catboost, xgboost
- dc_12: holdout N=4084, Brier=0.19281, selected=catboost, xgboost, logistic
- corners_o65: holdout N=4084, Brier=0.13042, selected=logistic, catboost, xgboost
- cards_o15: holdout N=4084, Brier=0.0975, selected=extra_trees, hist_gradient_boosting, catboost
- cards_o25: holdout N=4084, Brier=0.19171, selected=extra_trees, catboost, xgboost

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 12, "UNMAPPED_TEAM": 5}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "SP1", "fixture": "Deportivo vs Osasuna", "error": "UNMAPPED_TEAM", "unmapped_home": "Deportivo", "unmapped_away": null}
- [EXCLUSION] {"league": "SP2", "fixture": "Real Oviedo vs Las Palmas", "error": "UNMAPPED_TEAM", "unmapped_home": "Real Oviedo", "unmapped_away": null}
- [EXCLUSION] {"league": "SP2", "fixture": "Real Valladolid vs Leganés", "error": "UNMAPPED_TEAM", "unmapped_home": "Real Valladolid", "unmapped_away": null}
- [INFO] {"league": "I2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "F2", "fixture": "Red Star FC 93 vs AS Nancy Lorraine", "error": "UNMAPPED_TEAM", "unmapped_home": "Red Star FC 93", "unmapped_away": "AS Nancy Lorraine"}
- [EXCLUSION] {"league": "F2", "fixture": "Stade de Reims vs Sochaux", "error": "UNMAPPED_TEAM", "unmapped_home": "Stade de Reims", "unmapped_away": null}
- [INFO] {"league": "N1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "B1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
