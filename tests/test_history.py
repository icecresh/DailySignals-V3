from daily_signals.history import parse_matches, labels
from daily_signals.validation import walk_forward
def test_missing_ht_is_not_zero():
    row = parse_matches("Team 1,Team 2,FT,HT,UTC\nA,B,2-1,,2024-01-01T15:00Z\n", "test", "2024")[0]
    assert labels(row)["fh_o05"] is None
    assert labels(row)["ft_o25"] == 1
def test_unplayed_excluded():
    assert parse_matches("Team 1,Team 2,FT,HT,UTC\nA,B,-,,2024-01-01T15:00Z\n", "test", "2024") == []
def test_no_prediction_without_history():
    rows = parse_matches("Team 1,Team 2,FT,HT,UTC\nA,B,2-1,1-0,2024-01-01T15:00Z\n", "test", "2024")
    assert walk_forward(rows, min_history=1) == []
