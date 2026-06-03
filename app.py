"""Tkinter GUI for a Rock-Paper-Scissors game."""

from __future__ import annotations

import tkinter as tk

from rps_game import CHOICES, play_round

EMOJI_BY_CHOICE = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
}

TAGLINE_BY_CHOICE = {
    "rock": "Crushes scissors",
    "paper": "Covers rock",
    "scissors": "Cuts paper",
}

COLORS = {
    "background": "#0f172a",
    "panel": "#172033",
    "panel_light": "#202b44",
    "text": "#f8fafc",
    "muted": "#b6c2d9",
    "accent": "#38bdf8",
    "accent_dark": "#0ea5e9",
    "win": "#22c55e",
    "lose": "#fb7185",
    "tie": "#facc15",
}

OUTCOME_COLORS = {
    "win": COLORS["win"],
    "lose": COLORS["lose"],
    "tie": COLORS["tie"],
}


class RockPaperScissorsApp(tk.Tk):
    """Interactive Rock-Paper-Scissors desktop application."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Rock-Paper-Scissors")
        self.geometry("760x620")
        self.minsize(680, 580)
        self.configure(bg=COLORS["background"])

        self.wins = 0
        self.losses = 0
        self.ties = 0

        self.player_choice = tk.StringVar(value="—")
        self.computer_choice = tk.StringVar(value="—")
        self.result_text = tk.StringVar(value="Choose your fighter to start the match!")
        self.score_values: dict[str, tk.StringVar] = {
            "wins": tk.StringVar(value="0"),
            "losses": tk.StringVar(value="0"),
            "ties": tk.StringVar(value="0"),
        }
        self.result_label: tk.Label | None = None

        self._build_ui()

    def _build_ui(self) -> None:
        shell = tk.Frame(self, bg=COLORS["background"], padx=28, pady=26)
        shell.pack(fill="both", expand=True)

        card = tk.Frame(shell, bg=COLORS["panel"], padx=32, pady=30)
        card.pack(fill="both", expand=True)

        tk.Label(
            card,
            text="⚡ Rock-Paper-Scissors",
            bg=COLORS["panel"],
            fg=COLORS["text"],
            font=("Helvetica", 28, "bold"),
        ).pack(pady=(0, 8))

        tk.Label(
            card,
            text="A brighter battle arena with score cards, bold choices, and instant round feedback.",
            bg=COLORS["panel"],
            fg=COLORS["muted"],
            font=("Helvetica", 12),
            wraplength=560,
            justify="center",
        ).pack(pady=(0, 24))

        self._build_scoreboard(card)
        self._build_choice_buttons(card)
        self._build_round_panel(card)

        tk.Button(
            card,
            text="Reset score",
            command=self.reset_score,
            bg="#334155",
            fg=COLORS["text"],
            activebackground="#475569",
            activeforeground=COLORS["text"],
            bd=0,
            relief="flat",
            cursor="hand2",
            font=("Helvetica", 11, "bold"),
            padx=22,
            pady=10,
        ).pack(pady=(22, 0))

    def _build_scoreboard(self, parent: tk.Frame) -> None:
        scoreboard = tk.Frame(parent, bg=COLORS["panel"])
        scoreboard.pack(fill="x", pady=(0, 24))

        score_data = (
            ("wins", "Wins", COLORS["win"]),
            ("losses", "Losses", COLORS["lose"]),
            ("ties", "Ties", COLORS["tie"]),
        )
        for column, (key, label, color) in enumerate(score_data):
            scoreboard.columnconfigure(column, weight=1)
            score_card = tk.Frame(scoreboard, bg=COLORS["panel_light"], padx=18, pady=14)
            score_card.grid(row=0, column=column, sticky="ew", padx=6)

            tk.Label(
                score_card,
                text=label.upper(),
                bg=COLORS["panel_light"],
                fg=COLORS["muted"],
                font=("Helvetica", 9, "bold"),
            ).pack()
            tk.Label(
                score_card,
                textvariable=self.score_values[key],
                bg=COLORS["panel_light"],
                fg=color,
                font=("Helvetica", 24, "bold"),
            ).pack()

    def _build_choice_buttons(self, parent: tk.Frame) -> None:
        choices_frame = tk.Frame(parent, bg=COLORS["panel"])
        choices_frame.pack(fill="x", pady=(0, 26))

        for column, choice in enumerate(CHOICES):
            choices_frame.columnconfigure(column, weight=1)
            button = tk.Button(
                choices_frame,
                text=f"{EMOJI_BY_CHOICE[choice]}\n{choice.title()}\n{TAGLINE_BY_CHOICE[choice]}",
                command=lambda selected=choice: self.play(selected),
                bg=COLORS["accent_dark"],
                fg=COLORS["text"],
                activebackground=COLORS["accent"],
                activeforeground=COLORS["background"],
                bd=0,
                relief="flat",
                cursor="hand2",
                font=("Helvetica", 13, "bold"),
                padx=16,
                pady=18,
                justify="center",
            )
            button.grid(row=0, column=column, sticky="nsew", padx=8)

    def _build_round_panel(self, parent: tk.Frame) -> None:
        round_panel = tk.Frame(parent, bg=COLORS["background"], padx=18, pady=18)
        round_panel.pack(fill="x")

        picks = tk.Frame(round_panel, bg=COLORS["background"])
        picks.pack(fill="x")

        self._build_pick_card(picks, 0, "You picked", self.player_choice)
        self._build_pick_card(picks, 1, "Computer picked", self.computer_choice)

        self.result_label = tk.Label(
            round_panel,
            textvariable=self.result_text,
            bg=COLORS["background"],
            fg=COLORS["accent"],
            font=("Helvetica", 18, "bold"),
            wraplength=560,
            justify="center",
        )
        self.result_label.pack(pady=(22, 0))

    def _build_pick_card(
        self,
        parent: tk.Frame,
        column: int,
        title: str,
        choice_variable: tk.StringVar,
    ) -> None:
        parent.columnconfigure(column, weight=1)
        card = tk.Frame(parent, bg=COLORS["panel_light"], padx=16, pady=14)
        card.grid(row=0, column=column, sticky="ew", padx=7)

        tk.Label(
            card,
            text=title.upper(),
            bg=COLORS["panel_light"],
            fg=COLORS["muted"],
            font=("Helvetica", 9, "bold"),
        ).pack()
        tk.Label(
            card,
            textvariable=choice_variable,
            bg=COLORS["panel_light"],
            fg=COLORS["text"],
            font=("Helvetica", 18, "bold"),
        ).pack(pady=(6, 0))

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

        self._refresh_score()
        self._set_result_color(result.outcome)

    def reset_score(self) -> None:
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.player_choice.set("—")
        self.computer_choice.set("—")
        self.result_text.set("Score reset. Choose your next fighter!")
        self._refresh_score()
        self._set_result_color("ready")

    def _refresh_score(self) -> None:
        self.score_values["wins"].set(str(self.wins))
        self.score_values["losses"].set(str(self.losses))
        self.score_values["ties"].set(str(self.ties))

    def _set_result_color(self, outcome: str) -> None:
        if self.result_label is None:
            return
        self.result_label.configure(fg=OUTCOME_COLORS.get(outcome, COLORS["accent"]))

    @staticmethod
    def _display_choice(choice: str) -> str:
        return f"{EMOJI_BY_CHOICE[choice]} {choice.title()}"


if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.mainloop()
