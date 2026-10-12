# Nordic expansion — source qualification (2026-10-12)

Target: Norway Eliteserien (nor.1), Denmark Superliga (den.1), Sweden Allsvenskan (swe.1).

## Source research
- football-data.co.uk/all_new_data.php lists Norway, Denmark and Sweden in its extended data catalogue. **Not assumed to have HC/AC/HY/AY or HTHG/HTAG**. Inspect downloaded column headers and licence before using.
- cornerflick.com/data describes per-match `stats.csv`, `events.csv`, and season results, CC BY 4.0 for its compilation, while explicitly noting underlying provider rights. Danish 2026 results currently list only 47 records; a single season is insufficient for our three-year historical gate.
- footystats.org publishes multi-season Norwegian and Swedish datasets, but says automated retrieval should use its API; API rights and detailed columns must be confirmed.
- These sources are candidates, not approved ingestion feeds.

## Fail-closed validation procedure
1. Obtain lawful historical match-level files for 2023–2026, including fixture date, home/away identity, FTHG, FTAG, HTHG, HTAG, HC, AC, HY, AY.
2. Normalize headers into canonical format; preserve original source, retrieval date, licence/terms, and missingness.
3. Run `python scripts/validate_nordic.py --nor <file> --den <file> --swe <file>`.
4. Require >=600 valid matches, >=3 calendar years, >=95% completeness in each of the eight outcome columns, and zero invalid/duplicate rows. This is **data qualification only**.
5. Conduct chronological train/calibration/holdout evaluation for all 13 market definitions (six categories) on the expanded corpus; inspect league-specific corner reliability and sample sizes.
6. Verify ESPN prematch fixture availability, deterministic team-name mappings, and no post-kickoff leakage.
7. Only after passing every gate, add league codes to active `LEAGUES`, and perform a real GitHub Actions dry run.

## Current disposition
**NOT ACTIVATED** — no compliant, sufficiently complete three-season Nordic match-level files have been obtained or evaluated. Existing 19-league production schedule remains unchanged.

Sources:
- https://www.football-data.co.uk/all_new_data.php
- https://cornerflick.com/data
- https://cornerflick.com/football/leagues/danish-superliga/results
- https://footystats.org/norway/eliteserien/datasets
- https://footystats.org/sweden/allsvenskan/datasets
