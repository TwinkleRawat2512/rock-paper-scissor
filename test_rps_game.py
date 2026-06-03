import pytest

from rps_game import decide_winner, play_round


def test_decide_winner_all_outcomes():
    assert decide_winner("rock", "scissors") == "win"
    assert decide_winner("paper", "scissors") == "lose"
    assert decide_winner("scissors", "scissors") == "tie"


def test_play_round_returns_message_and_choices():
    result = play_round("paper", "rock")

    assert result.player_choice == "paper"
    assert result.computer_choice == "rock"
    assert result.outcome == "win"
    assert "You win" in result.message


def test_invalid_choice_raises_error():
    with pytest.raises(ValueError):
        play_round("lizard", "rock")
