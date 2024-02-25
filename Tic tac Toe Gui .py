import tkinter as tk
import tkinter.messagebox as msgbox
import random

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("300x300")
        self.board = ['-','-','-','-','-','-','-','-','-']
        self.current_player = 'X'
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self, text='', width=10, height=3, font=('Arial', 12), command=lambda i=i, j=j: self.make_move(i*3 + j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, idx):
        if self.board[idx] == '-' and not self.check_winner():
            self.board[idx] = self.current_player
            self.buttons[idx//3][idx%3].config(text=self.current_player)
            if self.check_winner():
                msgbox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif '-' not in self.board:
                msgbox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '-':
                return True
        return False

    def reset_board(self):
        self.board = ['-','-','-','-','-','-','-','-','-']
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
        self.current_player = 'X'

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
