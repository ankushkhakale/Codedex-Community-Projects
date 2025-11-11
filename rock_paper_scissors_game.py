"""
Rock Paper Scissors command-line game.

Player types their choice (rock, paper, scissors) or "quit" to exit.
Computer chooses randomly. The script prints round results and keeps score.
"""

import random
from typing import Literal, Tuple

Move = Literal["rock", "paper", "scissors"]


VALID_MOVES = ("rock", "paper", "scissors")


def normalize_move(text: str) -> str:
	"""Normalize user input to a lowercase move string.

	Returns the normalized move if valid, otherwise an empty string.
	"""
	if not isinstance(text, str):
		return ""
	t = text.strip().lower()
	return t if t in VALID_MOVES else ""


def get_computer_move() -> Move:
	"""Randomly choose and return a move for the computer."""
	return random.choice(VALID_MOVES)


def get_winner(player: Move, computer: Move) -> Literal["player", "computer", "tie"]:
	"""Return the winner given player and computer moves.

	- 'player' if player wins
	- 'computer' if computer wins
	- 'tie' if same move
	"""
	if player == computer:
		return "tie"

	# rock beats scissors, scissors beats paper, paper beats rock
	wins_against = {
		"rock": "scissors",
		"scissors": "paper",
		"paper": "rock",
	}

	return "player" if wins_against[player] == computer else "computer"


def format_round_result(player_move: Move, computer_move: Move) -> str:
	"""Return a human-friendly result string for a single round."""
	winner = get_winner(player_move, computer_move)
	if winner == "tie":
		return f"Tie! Both chose {player_move}."
	if winner == "player":
		return f"You win! {player_move.capitalize()} beats {computer_move}."
	return f"Computer wins! {computer_move.capitalize()} beats {player_move}."


def main() -> None:
	print("Welcome to Rock Paper Scissors! Type 'quit' to exit.")
	player_score = 0
	computer_score = 0
	round_number = 0

	while True:
		user = input("Enter your move (rock/paper/scissors or r/p/s) or 'quit': ")
		if user is None:
			# Defensive: treat as quit
			break
		u = user.strip().lower()
		if u == "quit":
			break
		# allow short forms
		short_map = {"r": "rock", "p": "paper", "s": "scissors"}
		if u in short_map:
			user = short_map[u]

		if user is None:
			# Defensive: treat as quit
			break
		if user.strip().lower() == "quit":
			break

		player_move = normalize_move(user)
		if not player_move:
			print("Invalid move. Please enter 'rock', 'paper', or 'scissors'.")
			continue

		computer_move = get_computer_move()
		round_number += 1

		result_txt = format_round_result(player_move, computer_move)
		print(result_txt)

		winner = get_winner(player_move, computer_move)
		if winner == "player":
			player_score += 1
		elif winner == "computer":
			computer_score += 1

		print(f"Score -> You: {player_score}  Computer: {computer_score}  (Rounds: {round_number})")
		print("")

	print("Thanks for playing!")
	print(f"Final score -> You: {player_score}  Computer: {computer_score}  (Rounds: {round_number})")


if __name__ == "__main__":
	main()

