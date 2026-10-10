from daily_signals.bayes import estimate
def test_future_results_never_used():
    row = {"kickoff":"2024-01-01T12:00:00+00:00","competition":"E","home":"A","away":"B",
           "home_goals":4,"away_goals":2,"home_ht_goals":2,"away_ht_goals":1}
    assert estimate([row], row, "ft_o15")["status"] == "UNAVAILABLE"
def test_no_fabricated_cards():
    assert estimate([], {"kickoff":"2024-01-01T12:00:00+00:00","competition":"E",
      "home":"A","away":"B"}, "cards_o25")["reason"] == "UNSUPPORTED_MARKET"
