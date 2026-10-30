# Daily Signals V3 — 2026-10-30

As of UTC: 2026-10-30T10:57:30.568462+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21447
Upcoming mapped fixtures: 5
Evaluated cells: 65
Research-qualified candidates: 26

## Research candidates — NOT publication-approved

- Newport County vs Chesterfield | cards_o15 | research estimate 90.4% | extra_trees, catboost, xgboost
- Lille vs Lens | cards_o15 | research estimate 90.4% | extra_trees, catboost, xgboost
- Nice vs Stade Rennais | cards_o15 | research estimate 88.9% | extra_trees, catboost, xgboost
- Sheffield United vs Wrexham | cards_o15 | research estimate 87.0% | extra_trees, catboost, xgboost
- Stenhousemuir vs Livingston | cards_o25 | research estimate 80.1% | extra_trees, catboost, xgboost
- Sheffield United vs Wrexham | corners_o65 | research estimate 88.1% | logistic, catboost, hist_gradient_boosting
- Nice vs Stade Rennais | corners_o65 | research estimate 88.1% | logistic, catboost, hist_gradient_boosting
- Newport County vs Chesterfield | corners_o65 | research estimate 84.3% | logistic, catboost, hist_gradient_boosting
- Lille vs Lens | corners_o65 | research estimate 83.2% | logistic, catboost, hist_gradient_boosting
- Stenhousemuir vs Livingston | corners_o65 | research estimate 81.9% | logistic, catboost, hist_gradient_boosting
- Sheffield United vs Wrexham | dc_12 | research estimate 73.4% | catboost, logistic, xgboost
- Newport County vs Chesterfield | dc_12 | research estimate 73.2% | catboost, logistic, xgboost
- Nice vs Stade Rennais | dc_12 | research estimate 73.2% | catboost, logistic, xgboost
- Lille vs Lens | dc_12 | research estimate 73.2% | catboost, logistic, xgboost
- Stenhousemuir vs Livingston | dc_12 | research estimate 73.2% | catboost, logistic, xgboost
- Stenhousemuir vs Livingston | dc_1x | research estimate 73.5% | logistic, xgboost, catboost
- Newport County vs Chesterfield | dc_x2 | research estimate 73.9% | logistic, catboost, xgboost
- Nice vs Stade Rennais | fh_o05 | research estimate 72.0% | catboost, xgboost, logistic
- Sheffield United vs Wrexham | fh_o05 | research estimate 71.9% | catboost, xgboost, logistic
- Newport County vs Chesterfield | fh_o05 | research estimate 71.9% | catboost, xgboost, logistic
- Lille vs Lens | fh_o05 | research estimate 71.9% | catboost, xgboost, logistic
- Nice vs Stade Rennais | ft_o15 | research estimate 76.8% | logistic, catboost, extra_trees
- Lille vs Lens | ft_o15 | research estimate 76.8% | logistic, catboost, extra_trees
- Sheffield United vs Wrexham | ft_o15 | research estimate 76.6% | logistic, catboost, extra_trees
- Newport County vs Chesterfield | ft_o15 | research estimate 72.2% | logistic, catboost, extra_trees
- Stenhousemuir vs Livingston | ft_o15 | research estimate 72.0% | logistic, catboost, extra_trees

## Holdout research validation

- fh_o05: holdout N=4006, Brier=0.20245, selected=catboost, xgboost, logistic
- ft_o15: holdout N=4006, Brier=0.17389, selected=logistic, catboost, extra_trees
- ft_o25: holdout N=4006, Brier=0.24362, selected=catboost, logistic, extra_trees
- btts: holdout N=4006, Brier=0.24635, selected=logistic, catboost, extra_trees
- home_win: holdout N=4006, Brier=0.23014, selected=logistic, catboost, xgboost
- draw: holdout N=4006, Brier=0.19405, selected=catboost, logistic, xgboost
- away_win: holdout N=4006, Brier=0.19728, selected=logistic, xgboost, catboost
- dc_1x: holdout N=4006, Brier=0.19729, selected=logistic, xgboost, catboost
- dc_x2: holdout N=4006, Brier=0.23021, selected=logistic, catboost, xgboost
- dc_12: holdout N=4006, Brier=0.19397, selected=catboost, logistic, xgboost
- corners_o65: holdout N=4006, Brier=0.13168, selected=logistic, catboost, hist_gradient_boosting
- cards_o15: holdout N=4006, Brier=0.09733, selected=extra_trees, catboost, xgboost
- cards_o25: holdout N=4006, Brier=0.19195, selected=extra_trees, catboost, xgboost

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 9, "UNMAPPED_TEAM": 12}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "D1", "fixture": "SV Elversberg vs Mainz", "error": "UNMAPPED_TEAM", "unmapped_home": "SV Elversberg", "unmapped_away": null}
- [EXCLUSION] {"league": "D2", "fixture": "Arminia Bielefeld vs TSV Eintracht Braunschweig", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "TSV Eintracht Braunschweig"}
- [EXCLUSION] {"league": "D2", "fixture": "Energie Cottbus vs VfL Bochum", "error": "UNMAPPED_TEAM", "unmapped_home": "Energie Cottbus", "unmapped_away": null}
- [EXCLUSION] {"league": "SP1", "fixture": "Villarreal vs Espanyol", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Espanyol"}
- [INFO] {"league": "SP2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "I1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "I2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "F1", "fixture": "Le Havre AC vs Paris Saint-Germain", "error": "UNMAPPED_TEAM", "unmapped_home": "Le Havre AC", "unmapped_away": "Paris Saint-Germain"}
- [EXCLUSION] {"league": "F2", "fixture": "Grenoble vs Dijon FCO", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Dijon FCO"}
- [EXCLUSION] {"league": "F2", "fixture": "Metz vs Pau", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Pau"}
- [EXCLUSION] {"league": "F2", "fixture": "Nantes vs Clermont Foot", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Clermont Foot"}
- [EXCLUSION] {"league": "F2", "fixture": "Rodez Aveyron vs Dunkerque", "error": "UNMAPPED_TEAM", "unmapped_home": "Rodez Aveyron", "unmapped_away": null}
- [EXCLUSION] {"league": "F2", "fixture": "Stade Laval vs Boulogne", "error": "UNMAPPED_TEAM", "unmapped_home": "Stade Laval", "unmapped_away": null}
- [INFO] {"league": "N1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "B1", "fixture": "Zulte-Waregem vs Club Brugge", "error": "UNMAPPED_TEAM", "unmapped_home": "Zulte-Waregem", "unmapped_away": null}
- [EXCLUSION] {"league": "P1", "fixture": "Casa Pia vs Sporting CP", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Sporting CP"}
- [INFO] {"league": "SC0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
