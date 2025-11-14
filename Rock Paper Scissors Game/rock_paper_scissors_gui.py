# python
import random
import tkinter as tk

MOVES = ("rock", "paper", "scissors")
wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

def get_winner(player, computer):
    if player == computer:
        return "tie"
    return "player" if wins[player] == computer else "computer"

class RPSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.player_score = 0
        self.computer_score = 0

        self.result_label = tk.Label(self, text="Choose: rock, paper, or scissors")
        self.result_label.pack(padx=10, pady=6)

        btn_frame = tk.Frame(self)
        btn_frame.pack()
        for m in MOVES:
            tk.Button(btn_frame, text=m.capitalize(), command=lambda mv=m: self.play(mv)).pack(side="left", padx=4)

        self.score_label = tk.Label(self, text="Score - You: 0  Computer: 0")
        self.score_label.pack(pady=6)
        tk.Button(self, text="Quit", command=self.destroy).pack(pady=4)

    def play(self, player_move):
        comp = random.choice(MOVES)
        winner = get_winner(player_move, comp)
        if winner == "player":
            self.player_score += 1
            res = f"You win! {player_move} beats {comp}."
        elif winner == "computer":
            self.computer_score += 1
            res = f"Computer wins! {comp} beats {player_move}."
        else:
            res = f"Tie! Both chose {player_move}."
        self.result_label.config(text=f"Computer chose {comp}. {res}")
        self.score_label.config(text=f"Score - You: {self.player_score}  Computer: {self.computer_score}")

if __name__ == "__main__":
    RPSApp().mainloop()