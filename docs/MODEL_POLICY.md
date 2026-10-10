# Daily Signals V3 model policy
All seven market families are in scope from day one. Candidate algorithms are not deployed or validated by registration.
- Goal score distributions must yield coherent FT totals, BTTS, H/D/A and double chance.
- Cards definition currently means **yellow cards only**. Red-card treatment requires an explicit agreed counting rule before publication.
- Never include bookmaker odds, implied odds, or tipster picks as training features.
- Use historical features only from before kickoff, and split train/calibration/holdout chronologically.
- Compare candidate models on the same eligible fixture-market rows.
- Model selection and stacking weights must be learned without holdout leakage.
- No publication without out-of-time calibration, coverage checks and quality gates.
- Corners Over 6.5; cards Over 2.5 preferred, otherwise Over 1.5; max one card signal per fixture.
- Keep MatchSignalAD repository, models and audits completely separate.
- Data provenance: https://www.football-data.co.uk/ ; raw CSV files must be checked for completeness and licensing.
