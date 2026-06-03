"""Core game logic for Rock-Paper-Scissors-Lizard-Spock."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable

CHOICES: tuple[str, ...] = ("rock", "paper", "scissors", "lizard", "spock")
WINNING_MATCHUPS: dict[str, dict[str, str]] = {
    "rock": {
        "scissors": "crushes",
        "lizard": "crushes",
    },
    "paper": {
        "rock": "covers",
        "spock": "disproves",
    },
    "scissors": {
        "paper": "cuts",
        "lizard": "decapitates",
    },
    "lizard": {
        "paper": "eats",
        "spock": "poisons",
    },
    "spock": {
        "rock": "vaporizes",
        "scissors": "smashes",
    },
}


@dataclass(frozen=True)
class RoundResult:
    """Result data for one round of Rock-Paper-Scissors-Lizard-Spock."""

    player_choice: str
    computer_choice: str
    outcome: str
    message: str


def normalize_choice(choice: str) -> str:
    """Return a cleaned, lowercase choice and validate that it is playable."""
    normalized = choice.strip().lower()
    if normalized not in CHOICES:
        valid_choices = ", ".join(CHOICES)
        raise ValueError(f"Choose one of: {valid_choices}.")
    return normalized


def get_computer_choice(choices: Iterable[str] = CHOICES) -> str:
    """Pick the computer's move at random."""
    return random.choice(tuple(choices))


def decide_winner(player_choice: str, computer_choice: str) -> str:
    """Return win, lose, or tie for the player's round outcome."""
    player = normalize_choice(player_choice)
    computer = normalize_choice(computer_choice)

    if player == computer:
        return "tie"
    if computer in WINNING_MATCHUPS[player]:
        return "win"
    return "lose"


def describe_matchup(winning_choice: str, losing_choice: str) -> str:
    """Return a sentence fragment explaining why one choice beats another."""
    winner = normalize_choice(winning_choice)
    loser = normalize_choice(losing_choice)
    action = WINNING_MATCHUPS[winner][loser]
    return f"{winner.title()} {action} {loser.title()}."


def play_round(player_choice: str, computer_choice: str | None = None) -> RoundResult:
    """Play one round and return a display-friendly result."""
    player = normalize_choice(player_choice)
    computer = normalize_choice(computer_choice) if computer_choice else get_computer_choice()
    outcome = decide_winner(player, computer)

    if outcome == "tie":
        message = "It's a tie!"
    elif outcome == "win":
        message = f"You win! {describe_matchup(player, computer)}"
    else:
        message = f"You lose! {describe_matchup(computer, player)}"

    return RoundResult(
        player_choice=player,
        computer_choice=computer,
        outcome=outcome,
        message=message,
    )
