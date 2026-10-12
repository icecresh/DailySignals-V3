# Daily Signals V3 — 2026-10-12

As of UTC: 2026-10-12T10:50:31.237548+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 20886
Upcoming mapped fixtures: 5
Evaluated cells: 65
Research-qualified candidates: 19

## Research candidates — NOT publication-approved

- Atalanta vs Venezia | cards_o15 | research estimate 89.4% | extra_trees, hist_gradient_boosting, catboost
- Torino vs Udinese | cards_o15 | research estimate 89.4% | extra_trees, hist_gradient_boosting, catboost
- Tenerife vs Girona | cards_o25 | research estimate 86.7% | catboost, extra_trees, hist_gradient_boosting
- Burgos vs Granada | cards_o25 | research estimate 86.2% | catboost, extra_trees, hist_gradient_boosting
- Levante vs Sevilla | cards_o25 | research estimate 81.5% | catboost, extra_trees, hist_gradient_boosting
- Levante vs Sevilla | corners_o65 | research estimate 85.2% | logistic, hist_gradient_boosting, catboost
- Tenerife vs Girona | corners_o65 | research estimate 80.6% | logistic, hist_gradient_boosting, catboost
- Atalanta vs Venezia | corners_o65 | research estimate 80.6% | logistic, hist_gradient_boosting, catboost
- Burgos vs Granada | corners_o65 | research estimate 78.3% | logistic, hist_gradient_boosting, catboost
- Torino vs Udinese | corners_o65 | research estimate 78.3% | logistic, hist_gradient_boosting, catboost
- Levante vs Sevilla | dc_12 | research estimate 72.9% | catboost, logistic, xgboost
- Atalanta vs Venezia | dc_12 | research estimate 72.9% | catboost, logistic, xgboost
- Torino vs Udinese | dc_12 | research estimate 72.9% | catboost, logistic, xgboost
- Burgos vs Granada | dc_1x | research estimate 76.6% | logistic, xgboost, extra_trees
- Levante vs Sevilla | ft_o15 | research estimate 73.9% | logistic, catboost, extra_trees
- Burgos vs Granada | ft_o15 | research estimate 73.0% | logistic, catboost, extra_trees
- Tenerife vs Girona | ft_o15 | research estimate 73.0% | logistic, catboost, extra_trees
- Torino vs Udinese | ft_o15 | research estimate 73.0% | logistic, catboost, extra_trees
- Atalanta vs Venezia | ft_o15 | research estimate 72.1% | logistic, catboost, extra_trees

## Holdout research validation

- fh_o05: holdout N=3916, Brier=0.20341, selected=catboost, xgboost, extra_trees
- ft_o15: holdout N=3916, Brier=0.17613, selected=logistic, catboost, extra_trees
- ft_o25: holdout N=3916, Brier=0.24555, selected=catboost, logistic, xgboost
- btts: holdout N=3916, Brier=0.2463, selected=catboost, logistic, extra_trees
- home_win: holdout N=3916, Brier=0.23022, selected=catboost, xgboost, random_forest
- draw: holdout N=3916, Brier=0.19514, selected=catboost, logistic, xgboost
- away_win: holdout N=3916, Brier=0.19852, selected=logistic, xgboost, extra_trees
- dc_1x: holdout N=3916, Brier=0.19848, selected=logistic, xgboost, extra_trees
- dc_x2: holdout N=3916, Brier=0.23022, selected=catboost, xgboost, random_forest
- dc_12: holdout N=3916, Brier=0.19514, selected=catboost, logistic, xgboost
- corners_o65: holdout N=3916, Brier=0.13086, selected=logistic, hist_gradient_boosting, catboost
- cards_o15: holdout N=3916, Brier=0.09584, selected=extra_trees, hist_gradient_boosting, catboost
- cards_o25: holdout N=3916, Brier=0.18998, selected=catboost, extra_trees, hist_gradient_boosting

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 13, "UNMAPPED_TEAM": 5}
- [EXCLUSION] {"league": "E0", "fixture": "Coventry City vs Newcastle United", "error": "UNMAPPED_TEAM", "unmapped_home": "Coventry City", "unmapped_away": null}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "SP2", "fixture": "Real Valladolid vs Albacete", "error": "UNMAPPED_TEAM", "unmapped_home": "Real Valladolid", "unmapped_away": null}
- [EXCLUSION] {"league": "SP2", "fixture": "Real Oviedo vs Eibar", "error": "UNMAPPED_TEAM", "unmapped_home": "Real Oviedo", "unmapped_away": null}
- [INFO] {"league": "I2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "F1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "F2", "fixture": "Dijon FCO vs Metz", "error": "UNMAPPED_TEAM", "unmapped_home": "Dijon FCO", "unmapped_away": null}
- [INFO] {"league": "N1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "B1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "P1", "fixture": "FC Famalicao vs Alverca", "error": "UNMAPPED_TEAM", "unmapped_home": "FC Famalicao", "unmapped_away": null}
- [INFO] {"league": "SC0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
