# Rock-Paper-Scissors-Lizard-Spock Game

A simple Python Rock-Paper-Scissors-Lizard-Spock game where a player competes against the computer.
The computer uses Python's `random` module to choose rock, paper, scissors, lizard, or Spock, and the game includes a Tkinter GUI for interactive play.

## Features

- Play rock, paper, scissors, lizard, or Spock against the computer.
- Randomized computer choices each round.
- Win, loss, and tie detection for the expanded Lizard-Spock rule set.
- Modern Tkinter interface with five bold choice cards, colorful score cards, round feedback, and a reset button.
- Reset button to clear the score and start fresh.
- Rules panel listing every winning interaction in the expanded game.


## Rules

Each gesture defeats two other moves and loses to the remaining two.

- Scissors cuts Paper
- Paper covers Rock
- Rock crushes Lizard
- Lizard poisons Spock
- Spock smashes Scissors
- Scissors decapitates Lizard
- Lizard eats Paper
- Paper disproves Spock
- Spock vaporizes Rock
- Rock crushes Scissors

## Run the game

```bash
python app.py
```

Tkinter is included with most standard Python installations. If the window does not open, ensure your Python installation includes Tk support.


## Run the online version

Open `web/index.html` directly in a browser, or serve the folder locally before deploying it to any static hosting service:

```bash
python -m http.server 8000 --directory web
```

Then visit `http://localhost:8000`.

## Project files

- `app.py` - Tkinter user interface.
- `rps_game.py` - Reusable game logic and random computer choices for all five moves.
- `web/` - Browser-based online version with HTML, CSS, and JavaScript.
