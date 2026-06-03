"""Tkinter GUI for a Rock-Paper-Scissors game."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from rps_game import CHOICES, play_round

EMOJI_BY_CHOICE = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
}


class RockPaperScissorsApp(tk.Tk):
    """Interactive Rock-Paper-Scissors desktop application."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Rock-Paper-Scissors")
        self.geometry("440x390")
        self.resizable(False, False)

        self.wins = 0
        self.losses = 0
        self.ties = 0

        self.player_choice = tk.StringVar(value="-")
        self.computer_choice = tk.StringVar(value="-")
        self.result_text = tk.StringVar(value="Choose rock, paper, or scissors to begin!")
        self.score_text = tk.StringVar(value=self._format_score())

        self._build_ui()

    def _build_ui(self) -> None:
        main = ttk.Frame(self, padding=24)
        main.pack(fill="both", expand=True)

        title = ttk.Label(
            main,
            text="Rock-Paper-Scissors",
            font=("Helvetica", 22, "bold"),
        )
        title.pack(pady=(0, 8))

        subtitle = ttk.Label(
            main,
            text="Play against the computer. The computer choice is randomized each round.",
            wraplength=360,
            justify="center",
        )
        subtitle.pack(pady=(0, 20))

        buttons = ttk.Frame(main)
        buttons.pack(pady=(0, 18))

        for choice in CHOICES:
            ttk.Button(
                buttons,
                text=f"{EMOJI_BY_CHOICE[choice]} {choice.title()}",
                command=lambda selected=choice: self.play(selected),
                width=14,
            ).pack(side="left", padx=5)

        picks = ttk.LabelFrame(main, text="Round choices", padding=12)
        picks.pack(fill="x", pady=(0, 18))

        ttk.Label(picks, text="You:", font=("Helvetica", 10, "bold")).grid(
            row=0, column=0, sticky="w", padx=(0, 8), pady=4
        )
        ttk.Label(picks, textvariable=self.player_choice).grid(row=0, column=1, sticky="w")

        ttk.Label(picks, text="Computer:", font=("Helvetica", 10, "bold")).grid(
            row=1, column=0, sticky="w", padx=(0, 8), pady=4
        )
        ttk.Label(picks, textvariable=self.computer_choice).grid(row=1, column=1, sticky="w")

        result = ttk.Label(
            main,
            textvariable=self.result_text,
            font=("Helvetica", 14, "bold"),
            wraplength=360,
            justify="center",
        )
        result.pack(pady=(0, 16))

        ttk.Label(main, textvariable=self.score_text, font=("Helvetica", 12)).pack(pady=(0, 14))
        ttk.Button(main, text="Reset score", command=self.reset_score).pack()

    def play(self, choice: str) -> None:
        result = play_round(choice)
        self.player_choice.set(self._display_choice(result.player_choice))
        self.computer_choice.set(self._display_choice(result.computer_choice))
        self.result_text.set(result.message)

        if result.outcome == "win":
            self.wins += 1
        elif result.outcome == "lose":
            self.losses += 1
        else:
            self.ties += 1

        self.score_text.set(self._format_score())

    def reset_score(self) -> None:
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.player_choice.set("-")
        self.computer_choice.set("-")
        self.result_text.set("Score reset. Choose your next move!")
        self.score_text.set(self._format_score())

    def _format_score(self) -> str:
        return f"Score — Wins: {self.wins}  Losses: {self.losses}  Ties: {self.ties}"

    @staticmethod
    def _display_choice(choice: str) -> str:
        return f"{EMOJI_BY_CHOICE[choice]} {choice.title()}"


if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.mainloop()
