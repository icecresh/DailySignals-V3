"""Regression tests for explicit ESPN-to-history club identity resolution."""
from scripts.v3_pipeline import resolve, fixtures
import scripts.v3_pipeline as pipeline
import json


def test_known_espn_name_variants():
    cases = {
        "Blackburn Rovers": "Blackburn",
        "Charlton Athletic": "Charlton",
        "Cardiff City": "Cardiff",
        "Swansea City": "Swansea",
        "Bolton Wanderers": "Bolton",
        "West Bromwich Albion": "West Brom",
        "Birmingham City": "Birmingham",
        "Preston North End": "Preston",
        "Stoke City": "Stoke",
        "Inverness Caledonian Thistle": "Inverness C",
    }
    for source, historical in cases.items():
        assert resolve(source, {historical}) == historical


def test_unknown_team_not_guessed():
    assert resolve("Unknown Athletic", {"Unknown City"}) is None


def test_wrong_date_fixture_is_excluded(monkeypatch):
    event = {"id": "123", "date": "2026-10-14T18:00:00Z",
             "status": {"type": {"state": "pre"}},
             "competitions": [{"competitors": [
                 {"homeAway": "home", "team": {"displayName": "Blackburn Rovers"}},
                 {"homeAway": "away", "team": {"displayName": "Charlton Athletic"}}]}]}
    monkeypatch.setattr(pipeline, "download", lambda url: json.dumps({"events": [event]}))
    matches = [{"league": "E1", "home": "Blackburn", "away": "Charlton"}]
    found, issues = fixtures("2026-10-13", {"E1": "eng.2"}, matches)
    assert found == []
    assert any(issue["error"] == "WRONG_FIXTURE_DATE" for issue in issues)
