"""Parse footballcsv historical results; preserve missing half-time scores."""
import csv
import re
from datetime import datetime, timezone
from io import StringIO
SCORE = re.compile(r"^(\d+)\s*-\s*(\d+)$")
def parse_matches(text, competition, season):
    out = []
    for row in csv.DictReader(StringIO(text)):
        ft = SCORE.fullmatch((row.get("FT") or "").strip())
        if not ft:
            continue
        try:
            kickoff = datetime.fromisoformat((row.get("UTC") or "").strip().replace("Z", "+00:00"))
        except ValueError:
            continue
        if kickoff.tzinfo is None:
            continue
        ht = SCORE.fullmatch((row.get("HT") or "").strip())
        home, away = (row.get("Team 1") or "").strip(), (row.get("Team 2") or "").strip()
        if not home or not away:
            continue
        out.append(dict(competition=competition, season=season,
            kickoff=kickoff.astimezone(timezone.utc).isoformat(), home=home, away=away,
            home_goals=int(ft[1]), away_goals=int(ft[2]),
            home_ht_goals=int(ht[1]) if ht else None, away_ht_goals=int(ht[2]) if ht else None))
    return sorted(out, key=lambda r: (r["kickoff"], r["home"], r["away"]))
def labels(row):
    hg, ag = row["home_goals"], row["away_goals"]
    return {"ft_o15": int(hg + ag >= 2), "ft_o25": int(hg + ag >= 3),
        "btts": int(hg > 0 and ag > 0),
        "result": "H" if hg > ag else "A" if ag > hg else "D",
        "fh_o05": None if row["home_ht_goals"] is None or row["away_ht_goals"] is None
        else int(row["home_ht_goals"] + row["away_ht_goals"] >= 1)}
