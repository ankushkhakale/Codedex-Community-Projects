"""Simple Tkinter GUI for the Rock Paper Scissors game.

This GUI reuses the logic in `rock_paper_scissors_game.py` (get_winner, etc.).
Run with: python rock_paper_scissors_gui.py
"""

import tkinter as tk
from tkinter import ttk
import random

import rock_paper_scissors_game as core


class RPSGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0
        self.rounds = 0

        main_frame = ttk.Frame(self, padding=12)
        main_frame.grid(row=0, column=0)

        self.info_label = ttk.Label(main_frame, text="Choose Rock, Paper or Scissors")
        self.info_label.grid(row=0, column=0, columnspan=3, pady=(0, 8))

        # Buttons
        self.buttons = {}
        for idx, move in enumerate(core.VALID_MOVES):
            b = ttk.Button(main_frame, text=move.capitalize(), command=lambda m=move: self.play(m))
            b.grid(row=1, column=idx, padx=6, pady=6)
            self.buttons[move] = b

        self.result_label = ttk.Label(main_frame, text="No rounds yet.")
        self.result_label.grid(row=2, column=0, columnspan=3, pady=(6, 6))

        self.score_label = ttk.Label(main_frame, text=self._score_text())
        self.score_label.grid(row=3, column=0, columnspan=3)

        quit_btn = ttk.Button(main_frame, text="Quit", command=self.destroy)
        quit_btn.grid(row=4, column=0, columnspan=3, pady=(8, 0))

    def _score_text(self) -> str:
        return f"Score — You: {self.player_score}    Computer: {self.computer_score}    Rounds: {self.rounds}"

    def play(self, player_move: str) -> None:
        # Use the same computer logic as the CLI
        comp_move = core.get_computer_move()
        winner = core.get_winner(player_move, comp_move)
        self.rounds += 1
        if winner == "player":
            self.player_score += 1
            round_msg = f"You win! {player_move.capitalize()} beats {comp_move}."
        elif winner == "computer":
            self.computer_score += 1
            round_msg = f"Computer wins! {comp_move.capitalize()} beats {player_move}."
        else:
            round_msg = f"Tie! Both chose {player_move}."

        self.result_label.config(text=f"Computer chose {comp_move}. {round_msg}")
        self.score_label.config(text=self._score_text())


def main():
    app = RPSGui()
    app.mainloop()


if __name__ == "__main__":
    main()
