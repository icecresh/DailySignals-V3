# Daily Signals V3 — 2026-10-16

As of UTC: 2026-10-16T08:15:12.128569+00:00

**NORMAL SIGNALS: No production-approved signals.**

Historical matches: 21069
Upcoming mapped fixtures: 8
Evaluated cells: 104
Research-qualified candidates: 40

## Research candidates — NOT publication-approved

- Frosinone vs Sassuolo | cards_o15 | research estimate 92.2% | extra_trees, hist_gradient_boosting, catboost
- Grenoble vs Boulogne | cards_o15 | research estimate 92.2% | extra_trees, hist_gradient_boosting, catboost
- Burnley vs Wolverhampton Wanderers | cards_o15 | research estimate 88.0% | extra_trees, hist_gradient_boosting, catboost
- Heerenveen vs Excelsior | cards_o15 | research estimate 87.3% | extra_trees, hist_gradient_boosting, catboost
- Leganés vs Córdoba | cards_o25 | research estimate 88.3% | extra_trees, catboost, hist_gradient_boosting
- Holstein Kiel vs Hertha Berlin | cards_o25 | research estimate 79.5% | extra_trees, catboost, hist_gradient_boosting
- Hellas Verona vs Catanzaro | cards_o25 | research estimate 79.5% | extra_trees, catboost, hist_gradient_boosting
- Le Mans vs Toulouse | cards_o25 | research estimate 79.5% | extra_trees, catboost, hist_gradient_boosting
- Burnley vs Wolverhampton Wanderers | corners_o65 | research estimate 88.0% | logistic, catboost, extra_trees
- Holstein Kiel vs Hertha Berlin | corners_o65 | research estimate 88.0% | logistic, catboost, extra_trees
- Heerenveen vs Excelsior | corners_o65 | research estimate 88.0% | logistic, catboost, extra_trees
- Hellas Verona vs Catanzaro | corners_o65 | research estimate 85.8% | logistic, catboost, extra_trees
- Le Mans vs Toulouse | corners_o65 | research estimate 85.8% | logistic, catboost, extra_trees
- Frosinone vs Sassuolo | corners_o65 | research estimate 82.4% | logistic, catboost, extra_trees
- Leganés vs Córdoba | corners_o65 | research estimate 77.8% | logistic, catboost, extra_trees
- Grenoble vs Boulogne | corners_o65 | research estimate 77.8% | logistic, catboost, extra_trees
- Burnley vs Wolverhampton Wanderers | dc_12 | research estimate 73.6% | catboost, logistic, xgboost
- Heerenveen vs Excelsior | dc_12 | research estimate 73.6% | catboost, logistic, xgboost
- Frosinone vs Sassuolo | dc_12 | research estimate 73.4% | catboost, logistic, xgboost
- Hellas Verona vs Catanzaro | dc_12 | research estimate 73.4% | catboost, logistic, xgboost
- Le Mans vs Toulouse | dc_12 | research estimate 73.4% | catboost, logistic, xgboost
- Holstein Kiel vs Hertha Berlin | dc_12 | research estimate 73.1% | catboost, logistic, xgboost
- Grenoble vs Boulogne | dc_12 | research estimate 71.0% | catboost, logistic, xgboost
- Leganés vs Córdoba | dc_12 | research estimate 70.7% | catboost, logistic, xgboost
- Frosinone vs Sassuolo | dc_1x | research estimate 77.6% | logistic, xgboost, catboost
- Hellas Verona vs Catanzaro | dc_1x | research estimate 77.3% | logistic, xgboost, catboost
- Grenoble vs Boulogne | dc_1x | research estimate 70.1% | logistic, xgboost, catboost
- Burnley vs Wolverhampton Wanderers | fh_o05 | research estimate 76.1% | xgboost, catboost, extra_trees
- Heerenveen vs Excelsior | fh_o05 | research estimate 76.1% | xgboost, catboost, extra_trees
- Holstein Kiel vs Hertha Berlin | fh_o05 | research estimate 72.2% | xgboost, catboost, extra_trees
- Hellas Verona vs Catanzaro | fh_o05 | research estimate 72.2% | xgboost, catboost, extra_trees
- Le Mans vs Toulouse | fh_o05 | research estimate 71.8% | xgboost, catboost, extra_trees
- Heerenveen vs Excelsior | ft_o15 | research estimate 88.1% | logistic, catboost, extra_trees
- Burnley vs Wolverhampton Wanderers | ft_o15 | research estimate 81.5% | logistic, catboost, extra_trees
- Holstein Kiel vs Hertha Berlin | ft_o15 | research estimate 81.5% | logistic, catboost, extra_trees
- Hellas Verona vs Catanzaro | ft_o15 | research estimate 81.5% | logistic, catboost, extra_trees
- Le Mans vs Toulouse | ft_o15 | research estimate 74.9% | logistic, catboost, extra_trees
- Frosinone vs Sassuolo | ft_o15 | research estimate 73.7% | logistic, catboost, extra_trees
- Leganés vs Córdoba | ft_o15 | research estimate 71.7% | logistic, catboost, extra_trees
- Grenoble vs Boulogne | ft_o15 | research estimate 71.7% | logistic, catboost, extra_trees

## Holdout research validation

- fh_o05: holdout N=3917, Brier=0.20305, selected=xgboost, catboost, extra_trees
- ft_o15: holdout N=3917, Brier=0.17515, selected=logistic, catboost, extra_trees
- ft_o25: holdout N=3917, Brier=0.24556, selected=catboost, logistic, extra_trees
- btts: holdout N=3917, Brier=0.24674, selected=catboost, logistic, extra_trees
- home_win: holdout N=3917, Brier=0.23131, selected=xgboost, catboost, lightgbm
- draw: holdout N=3917, Brier=0.19402, selected=catboost, logistic, xgboost
- away_win: holdout N=3917, Brier=0.19695, selected=logistic, xgboost, catboost
- dc_1x: holdout N=3917, Brier=0.19697, selected=logistic, xgboost, catboost
- dc_x2: holdout N=3917, Brier=0.23131, selected=xgboost, catboost, lightgbm
- dc_12: holdout N=3917, Brier=0.19403, selected=catboost, logistic, xgboost
- corners_o65: holdout N=3917, Brier=0.13061, selected=logistic, catboost, extra_trees
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
Fixture exclusion counts: {"NO_SCHEDULED_EVENTS": 8, "UNMAPPED_TEAM": 8}
- [INFO] {"league": "E0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "E3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "D1", "fixture": "Eintracht Frankfurt vs FC Cologne", "error": "UNMAPPED_TEAM", "unmapped_home": "Eintracht Frankfurt", "unmapped_away": null}
- [EXCLUSION] {"league": "D2", "fixture": "Energie Cottbus vs 1. FC Nürnberg", "error": "UNMAPPED_TEAM", "unmapped_home": "Energie Cottbus", "unmapped_away": "1. FC Nürnberg"}
- [EXCLUSION] {"league": "SP1", "fixture": "Deportivo vs Levante", "error": "UNMAPPED_TEAM", "unmapped_home": "Deportivo", "unmapped_away": null}
- [EXCLUSION] {"league": "F2", "fixture": "Annecy vs AS Nancy Lorraine", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "AS Nancy Lorraine"}
- [EXCLUSION] {"league": "F2", "fixture": "Guingamp vs Pau", "error": "UNMAPPED_TEAM", "unmapped_home": null, "unmapped_away": "Pau"}
- [EXCLUSION] {"league": "F2", "fixture": "Stade de Reims vs Dijon FCO", "error": "UNMAPPED_TEAM", "unmapped_home": "Stade de Reims", "unmapped_away": "Dijon FCO"}
- [EXCLUSION] {"league": "F2", "fixture": "Stade Laval vs Clermont Foot", "error": "UNMAPPED_TEAM", "unmapped_home": "Stade Laval", "unmapped_away": "Clermont Foot"}
- [INFO] {"league": "B1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "P1", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC0", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [EXCLUSION] {"league": "SC1", "fixture": "Ayr United vs Partick Thistle", "error": "UNMAPPED_TEAM", "unmapped_home": "Ayr United", "unmapped_away": "Partick Thistle"}
- [INFO] {"league": "SC2", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
- [INFO] {"league": "SC3", "error": "NO_SCHEDULED_EVENTS", "severity": "INFO"}
