from daily_signals.event_history import parse_event_csv,event_labels
from daily_signals.model_registry import candidate_registry
def test_events_and_missing_values():
    text="Date,HomeTeam,AwayTeam,FTHG,FTAG,HC,AC,HY,AY,HR,AR,Referee,B365H\n10/08/2024,A,B,2,1,5,4,2,1,0,1,Ref,1.5\n11/08/2024,C,D,1,0,,,1,1,,,Ref,2.1\n"
    rows=parse_event_csv(text,"E0","2425")
    assert len(rows)==2
    assert event_labels(rows[0])=={"corners_o65":1,"cards_o15":1,"cards_o25":1}
    assert event_labels(rows[1])["corners_o65"] is None
    assert "B365H" not in str(rows)
def test_registry_not_trained():
    r=candidate_registry()
    assert all(v["status"]=="NOT_TRAINED" for v in r.values())
    assert "corners_o65" in r and "cards_o25" in r
