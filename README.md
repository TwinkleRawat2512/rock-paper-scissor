# Rock-Paper-Scissors Game

A simple Python Rock-Paper-Scissors game where a player competes against the computer.
The computer uses Python's `random` module to choose rock, paper, or scissors, and the game includes a Tkinter GUI for interactive play.

## Features

- Play rock, paper, or scissors against the computer.
- Randomized computer choices each round.
- Win, loss, and tie detection.
- Modern Tkinter interface with bold choice cards, colorful score cards, round feedback, and a reset button.
- Reset button to clear the score and start fresh.

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
- `rps_game.py` - Reusable game logic and random computer choices.
- `web/` - Browser-based online version with HTML, CSS, and JavaScript.
