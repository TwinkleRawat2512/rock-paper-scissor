import pytest

from rps_game import CHOICES, RULES, WINNING_MATCHUPS, decide_winner, play_round


def test_decide_winner_all_standard_outcomes():
    assert decide_winner("rock", "scissors") == "win"
    assert decide_winner("paper", "scissors") == "lose"
    assert decide_winner("scissors", "scissors") == "tie"


def test_all_lizard_spock_matchups_are_supported():
    assert CHOICES == ("rock", "paper", "scissors", "lizard", "spock")

    for winner, defeated_choices in WINNING_MATCHUPS.items():
        assert len(defeated_choices) == 2
        for loser in defeated_choices:
            assert decide_winner(winner, loser) == "win"
            assert decide_winner(loser, winner) == "lose"


def test_rules_are_listed_in_requested_order():
    assert RULES == (
        ("scissors", "cuts", "paper"),
        ("paper", "covers", "rock"),
        ("rock", "crushes", "lizard"),
        ("lizard", "poisons", "spock"),
        ("spock", "smashes", "scissors"),
        ("scissors", "decapitates", "lizard"),
        ("lizard", "eats", "paper"),
        ("paper", "disproves", "spock"),
        ("spock", "vaporizes", "rock"),
        ("rock", "crushes", "scissors"),
    )


def test_play_round_returns_message_and_choices():
    result = play_round("lizard", "spock")

    assert result.player_choice == "lizard"
    assert result.computer_choice == "spock"
    assert result.outcome == "win"
    assert "Lizard poisons Spock" in result.message


def test_invalid_choice_raises_error():
    with pytest.raises(ValueError, match="lizard"):
        play_round("water", "rock")
