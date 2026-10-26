# Daily Signals V3 — 2026-10-26

As of UTC: 2026-10-26T10:12:06.022279+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21250
Upcoming mapped fixtures: 3
Evaluated cells: 39
Research-qualified candidates: 16

## Research candidates — NOT publication-approved

- FC Andorra vs Burgos | cards_o25 | research estimate 90.2% | extra_trees, catboost, hist_gradient_boosting
- Santa Clara vs Benfica | cards_o25 | research estimate 86.5% | extra_trees, catboost, hist_gradient_boosting
- Sevilla vs Osasuna | cards_o25 | research estimate 80.6% | extra_trees, catboost, hist_gradient_boosting
- Sevilla vs Osasuna | corners_o65 | research estimate 82.9% | logistic, catboost, xgboost
- Santa Clara vs Benfica | corners_o65 | research estimate 80.8% | logistic, catboost, xgboost
- FC Andorra vs Burgos | corners_o65 | research estimate 76.3% | logistic, catboost, xgboost
- Santa Clara vs Benfica | dc_12 | research estimate 73.3% | catboost, logistic, xgboost
- Sevilla vs Osasuna | dc_12 | research estimate 72.1% | catboost, logistic, xgboost
- Sevilla vs Osasuna | dc_1x | research estimate 73.9% | logistic, xgboost, catboost
- Santa Clara vs Benfica | dc_x2 | research estimate 78.6% | catboost, extra_trees, xgboost
- FC Andorra vs Burgos | dc_x2 | research estimate 75.4% | catboost, extra_trees, xgboost
- Santa Clara vs Benfica | fh_o05 | research estimate 75.5% | catboost, extra_trees, logistic
- Sevilla vs Osasuna | fh_o05 | research estimate 70.6% | catboost, extra_trees, logistic
- Santa Clara vs Benfica | ft_o15 | research estimate 77.9% | catboost, logistic, xgboost
- Sevilla vs Osasuna | ft_o15 | research estimate 74.6% | catboost, logistic, xgboost
- FC Andorra vs Burgos | ft_o15 | research estimate 72.0% | catboost, logistic, xgboost

## Holdout research validation

- fh_o05: holdout N=3944, Brier=0.2022, selected=catboost, extra_trees, logistic
- ft_o15: holdout N=3944, Brier=0.17464, selected=catboost, logistic, xgboost
- ft_o25: holdout N=3944, Brier=0.24464, selected=catboost, logistic, xgboost
- btts: holdout N=3944, Brier=0.2469, selected=catboost, logistic, extra_trees
- home_win: holdout N=3944, Brier=0.23118, selected=catboost, extra_trees, xgboost
- draw: holdout N=3944, Brier=0.19391, selected=catboost, logistic, xgboost
- away_win: holdout N=3944, Brier=0.19758, selected=logistic, xgboost, catboost
- dc_1x: holdout N=3944, Brier=0.19767, selected=logistic, xgboost, catboost
- dc_x2: holdout N=3944, Brier=0.23118, selected=catboost, extra_trees, xgboost
- dc_12: holdout N=3944, Brier=0.19388, selected=catboost, logistic, xgboost
- corners_o65: holdout N=3944, Brier=0.13196, selected=logistic, catboost, xgboost
- cards_o15: holdout N=3944, Brier=0.09825, selected=extra_trees, catboost, xgboost
- cards_o25: holdout N=3944, Brier=0.19171, selected=extra_trees, catboost, hist_gradient_boosting

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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 13, "UNMAPPED_TEAM": 4}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "E3", "fixture": "Walsall vs Salford City", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Salford City"}
- [INFO] {"league": "D1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "D2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "I1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "I2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "F1", "fixture": "Paris Saint-Germain vs Lyon", "error": "UNMAPPED_TEAM", "unmapped_home": "Paris Saint-Germain", "unmapped_away": null}
- [EXCLUSION] {"league": "F2", "fixture": "Boulogne vs Stade de Reims", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Stade de Reims"}
- [EXCLUSION] {"league": "F2", "fixture": "Montpellier vs Red Star FC 93", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Red Star FC 93"}
- [INFO] {"league": "N1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "B1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
