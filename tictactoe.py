import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.root.geometry("300x300")

        self.board = []
        self.buttons = []

        self.current_player = "X"

        for row in range(3):
            self.board.append([])
            for col in range(3):
                button = tk.Button(self.root, text="", width=10, height=5,
                                   command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.board[row].append(button)

        self.root.mainloop()

    def make_move(self, row, col):
        if self.board[row][col]["text"] == "":
            self.board[row][col]["text"] = self.current_player
            self.board[row][col].config(state="disable")

            if self.check_winner():
                messagebox.showinfo("Победа", f"Игрок {self.current_player} выиграл!")
                self.root.quit()
            elif self.check_draw():
                messagebox.showinfo("Ничья", "Ничья!")
                self.root.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.bot_move()

    def check_winner(self):
        lines = [
            [(0, 0), (0, 1), (0, 2)],  # Горизонтальные линии
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],

            [(0, 0), (1, 0), (2, 0)],  # Вертикальные линии
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],

            [(0, 0), (1, 1), (2, 2)],  # Диагональные линии
            [(0, 2), (1, 1), (2, 0)]
        ]

        for line in lines:
            symbols = [self.board[row][col]["text"] for row, col in line]
            if symbols == ["X", "X", "X"] or symbols == ["O", "O", "O"]:
                for row, col in line:
                    self.board[row][col].config()
                return True
        return False

    # проверка на ничью
    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col]["text"] == "":
                    return False
        return True

    def bot_move(self):
        best_score = float("-inf")
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.board[row][col]["text"] == "":
                    self.board[row][col]["text"] = "O"
                    score = self.minimax(0, False)
                    self.board[row][col]["text"] = ""

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        row, col = best_move
        self.board[row][col]["text"] = "O"
        self.board[row][col].config(state="disable")

        if self.check_winner():
            messagebox.showinfo("Поражение", "Вы проиграли!")
            self.root.quit()
        elif self.check_draw():
            messagebox.showinfo("Ничья", "Ничья!")
            self.root.quit()
        else:
            self.current_player = "X"

    def minimax(self, depth, is_maximizing):
        scores = {"X": -1, "O": 1, "draw": 0}

        if self.check_winner():
            return scores[self.current_player]

        if self.check_draw():
            return scores["draw"]

        if is_maximizing:
            best_score = float("-inf")

            for row in range(3):
                for col in range(3):
                    if self.board[row][col]["text"] == "":
                        self.board[row][col]["text"] = "O"
                        score = self.minimax(depth + 1, False)
                        self.board[row][col]["text"] = ""
                        best_score = max(score, best_score)

            return best_score
        else:
            best_score = float("inf")

            for row in range(3):
                for col in range(3):
                    if self.board[row][col]["text"] == "":
                        self.board[row][col]["text"] = "X"
                        if self.check_winner():
                            score = scores["X"]
                        else:
                            score = self.minimax(depth + 1, True)
                        self.board[row][col]["text"] = ""
                        best_score = min(score, best_score)

            return best_score

root = tk.Tk()
game = TicTacToe(root)