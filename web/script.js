const choices = ["rock", "paper", "scissors", "lizard", "spock"];
const winningMatchups = {
  rock: {
    scissors: "crushes",
    lizard: "crushes",
  },
  paper: {
    rock: "covers",
    spock: "disproves",
  },
  scissors: {
    paper: "cuts",
    lizard: "decapitates",
  },
  lizard: {
    paper: "eats",
    spock: "poisons",
  },
  spock: {
    rock: "vaporizes",
    scissors: "smashes",
  },
};
const emojiByChoice = {
  rock: "🪨",
  paper: "📄",
  scissors: "✂️",
  lizard: "🦎",
  spock: "🖖",
};

const score = {
  wins: 0,
  losses: 0,
  ties: 0,
};

const playerChoice = document.querySelector("#player-choice");
const computerChoice = document.querySelector("#computer-choice");
const resultMessage = document.querySelector("#result-message");
const resetButton = document.querySelector("#reset-button");
const scoreElements = {
  wins: document.querySelector("#wins"),
  losses: document.querySelector("#losses"),
  ties: document.querySelector("#ties"),
};

function getComputerChoice() {
  const randomIndex = Math.floor(Math.random() * choices.length);
  return choices[randomIndex];
}

function decideWinner(player, computer) {
  if (player === computer) {
    return "tie";
  }

  return winningMatchups[player][computer] ? "win" : "lose";
}

function formatChoice(choice) {
  return `${emojiByChoice[choice]} ${choice[0].toUpperCase()}${choice.slice(1)}`;
}

function describeMatchup(winner, loser) {
  return `${formatChoice(winner)} ${winningMatchups[winner][loser]} ${formatChoice(loser)}.`;
}

function buildMessage(outcome, player, computer) {
  if (outcome === "tie") {
    return "It's a tie! Try again.";
  }

  if (outcome === "win") {
    return `You win! ${describeMatchup(player, computer)}`;
  }

  return `You lose! ${describeMatchup(computer, player)}`;
}

function updateScore(outcome) {
  if (outcome === "win") {
    score.wins += 1;
  } else if (outcome === "lose") {
    score.losses += 1;
  } else {
    score.ties += 1;
  }

  scoreElements.wins.textContent = score.wins;
  scoreElements.losses.textContent = score.losses;
  scoreElements.ties.textContent = score.ties;
}

function setResultClass(outcome) {
  resultMessage.classList.remove("win", "lose", "tie");
  resultMessage.classList.add(outcome);
}

function playRound(player) {
  const computer = getComputerChoice();
  const outcome = decideWinner(player, computer);

  playerChoice.textContent = formatChoice(player);
  computerChoice.textContent = formatChoice(computer);
  resultMessage.textContent = buildMessage(outcome, player, computer);
  setResultClass(outcome);
  updateScore(outcome);
}

function resetGame() {
  score.wins = 0;
  score.losses = 0;
  score.ties = 0;
  playerChoice.textContent = "—";
  computerChoice.textContent = "—";
  resultMessage.textContent = "Pick a move to start the game.";
  resultMessage.classList.remove("win", "lose", "tie");
  scoreElements.wins.textContent = "0";
  scoreElements.losses.textContent = "0";
  scoreElements.ties.textContent = "0";
}

document.querySelectorAll("[data-choice]").forEach((button) => {
  button.addEventListener("click", () => playRound(button.dataset.choice));
});

resetButton.addEventListener("click", resetGame);
