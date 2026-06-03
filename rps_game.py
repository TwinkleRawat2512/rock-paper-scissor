"""Core game logic for Rock-Paper-Scissors."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable

CHOICES: tuple[str, ...] = ("rock", "paper", "scissors")
WINNING_MOVES: dict[str, str] = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


@dataclass(frozen=True)
class RoundResult:
    """Result data for one round of Rock-Paper-Scissors."""

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
    if WINNING_MOVES[player] == computer:
        return "win"
    return "lose"


def play_round(player_choice: str, computer_choice: str | None = None) -> RoundResult:
    """Play one round and return a display-friendly result."""
    player = normalize_choice(player_choice)
    computer = normalize_choice(computer_choice) if computer_choice else get_computer_choice()
    outcome = decide_winner(player, computer)

    if outcome == "tie":
        message = "It's a tie!"
    elif outcome == "win":
        message = f"You win! {player.title()} beats {computer}."
    else:
        message = f"You lose! {computer.title()} beats {player}."

    return RoundResult(
        player_choice=player,
        computer_choice=computer,
        outcome=outcome,
        message=message,
    )
