import tkinter as tk
from tkinter.messagebox import showinfo, askyesno
from PIL import ImageTk, Image

class RussianCheckers:
    def __init__(self, root):
        self.root = root
        root.title("Русские шашки-поддавки")
        root.geometry("750x600")
        root.resizable(0, 0)
        # root.eval('tk::PlaceWindow . center')
        root.config(bg='#6e5d91')

        self.black_piece_image = ImageTk.PhotoImage(Image.open('black_piece.png').resize((75, 85)))
        self.white_piece_image = ImageTk.PhotoImage(Image.open('white_piece.png').resize((75, 85)))
        self.white_bg = ImageTk.PhotoImage(Image.open('white_bg.jpg').resize((80, 85)))
        self.black_bg = ImageTk.PhotoImage(Image.open('black_bg.png').resize((80, 85)))

        self.board = []
        self.buttons = []
        self.turn_player = True # для игрока (1), false для бота (игрока 2)
        self.selected_piece = None
        self.available_bot_checkers = []

        self.label_status = tk.Label(root, text="", bg='#6e5d91', fg='#fff')
        self.label_status.place(x=200, y=570)
        # label кто играет (кто зашёл на акк) и количество побед и поражений
        # label чей ход
        # кнопка сдаться

        for row in range(8):
            self.board.append([])
            for col in range(8):
                if (row + col) % 2 == 0:
                    button = tk.Button(self.root, text="", width=70, height=65,
                                       command=lambda row=row, col=col: self.make_move(row, col),
                                       image=self.white_bg)
                    button.grid(row=row, column=col)
                    self.board[row].append(button)
                else:
                    button = tk.Button(self.root, text="", width=70, height=65,
                                       command=lambda row=row, col=col: self.make_move(row, col),
                                       image=self.black_bg)
                    button.grid(row=row, column=col)
                    self.board[row].append(button)
        self.setup_board()

        self.root.mainloop()

        # расположение шашек
    def setup_board(self):
        for row in range(8):
            for col in range(8):
                if row < 3 and (row + col) % 2 == 1:
                    self.board[row][col].configure(text="bot", fg="black", image=self.black_piece_image, width=70, height=65,
                                   command=lambda row=row, col=col: self.make_move(row, col))
                elif row > 4 and (row + col) % 2 == 1:
                    self.board[row][col].configure(text="player", fg="black", image=self.white_piece_image)

    def make_move(self, row, col):
        self.label_status.configure(text="")
        if self.selected_piece:
            row_source, col_source = self.selected_piece
            available = self.available_checkers(self.turn_player, row_source, col_source)
            if available:
                if abs(row_source - row) == 1 and abs(col_source - col) == 1 and self.board[row][col].cget("text") == "":
                    if self.make_normal_checker_move(row_source, col_source, row, col):
                        self.turn_player = not self.turn_player
                        if self.check_win(self.turn_player):
                            if self.turn_player:
                                result = askyesno(title="Информация", message="Победили белые.\n Начать новую игру?")
                                if result:
                                    self.root.destroy()
                                    root = tk.Tk()
                                    self.__init__(root)
                                else:
                                    exit()
                            elif self.turn_player:
                                result = askyesno(title="Информация", message="Победили красные.\n Начать новую игру?")
                                if result:
                                    self.root.destroy()
                                    root = tk.Tk()
                                    self.__init__(root)
                                else:
                                    exit()
                elif abs(row_source - row) == 2 and abs(col_source - col) == 2 and self.board[row][col].cget("text") == "":
                    self.capture_checker(col, row, row_source, col_source)
                else:
                    self.label_status.configure(text="Такой ход нельзя совершить")
            else:
                self.label_status.configure(text="Это чужая шашка")
            self.selected_piece = None
        else:
            if self.board[row][col].cget("text") != "":
                self.selected_piece = (row, col)



    def make_normal_checker_move(self, row_source, col_source, row, col):
        image_checkers = self.choice_image(self.turn_player, self.white_piece_image, self.black_piece_image)
        image_checker = image_checkers[0]
        piece = self.board[row_source][col_source].cget("text")

        # Проверяем, что шашка ходит по диагонали вперед на одну клетку
        if self.turn_player:
            if row_source - row == 1 and abs(col_source - col) == 1:
                self.board[row_source][col_source].configure(text="", image=self.black_bg)
                self.board[row][col].configure(text=piece, image=image_checker)
                return True
            else:
                self.label_status.configure(text="Шашка может ходить только по диагонали вперед на одну клетку")
                self.selected_piece = None
                return False
        else:
            if row - row_source == 1 and abs(col_source - col) == 1:
                self.board[row_source][col_source].configure(text="", image=self.black_bg)
                self.board[row][col].configure(text=piece, image=image_checker)
                return True
            else:
                self.label_status.configure(text="Шашка может ходить только по диагонали вперед на одну клетку")
                self.selected_piece = None
                return False

        # захват шашки
    def capture_checker(self, col, row, row_source, col_source):
        image_checkers = (self.choice_image(self.turn_player, self.white_piece_image, self.black_piece_image))
        image_checker = image_checkers[0]
        enemy_image = image_checkers[1]
        if abs(row_source - row) == 2:  # проверка на захват шашки противника
            eaten_row = (row + row_source) // 2  # вычисляем координаты съеденной шашки
            eaten_col = (col + col_source) // 2
            if self.board[eaten_row][eaten_col].cget("image") != self.board[row_source][col_source].cget("image"):
                piece = self.board[row_source][col_source].cget("text")  # выполнение перемещения шашки
                self.board[row_source][col_source].configure(text="", image=self.black_bg)
                self.board[row][col].configure(text=piece, image=image_checker)
                self.board[eaten_row][eaten_col].configure(text="", image=self.black_bg)  # удаляем съеденную шашку
            else:  # self.board[eaten_row][eaten_col].cget("text") != "" and self.board[eaten_row][eaten_col].cget("image") == self.black_piece_image:
                self.selected_piece = None
                self.label_status.configure(text="Нельзя кушать свои шашки")

            # if self.board[eaten_row][eaten_col].cget("text") != "" and ((self.board[eaten_row][eaten_col].cget("image") == self.black_piece_image or self.board[eaten_row][eaten_col].cget("image") == self.black_bg)):
            #     self.board[eaten_row][eaten_col].configure(text="", image=self.black_bg)  # Удаляем съеденную шашку

        else:
            self.selected_piece = None
            # self.label_status.configure(text="Нельзя кушать свои шашки")

    def choice_image(self, turn_player, white_piece_image, black_piece_image):
        if turn_player:
            image_checker = white_piece_image
            enemy_image = black_piece_image
        else:
            image_checker = black_piece_image
            enemy_image = white_piece_image
        return image_checker, enemy_image

    def available_checkers(self, turn_player, row, col):
        if turn_player and self.board[row][col].cget("text") == "player":
            return True
        elif not turn_player and self.board[row][col].cget("text") == "bot":
            return True
        else:
            return False

    def check_win(self, turn_player):
        if not turn_player:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    try:
                        if self.board[i][j].cget("text") == "player":

                            if self.board[i - 1][j + 1].cget("text") == "" or self.board[i - 1][j - 1].cget("text") == "":
                                return False
                            elif (self.board[i - 1][j + 1].cget("text") == 'player' and self.board[i - 2][j + 2].cget("text") == "") or (self.board[i - 1][j - 1].cget("text") == 'player' and self.board[i - 2][j - 2].cget("text") == ""):
                                return False
                    except IndexError:
                        pass
            return True
        if turn_player:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    try:
                        if self.board[i][j].cget("text") == "bot":
                            if self.board[i + 1][j + 1].cget("text") == "" or self.board[i + 1][j - 1].cget("text") == "":
                                return False
                            elif (self.board[i + 1][j + 1].cget("text") == 'bot' and self.board[i + 2][j + 2].cget("text") == "") or (self.board[i + 1][j - 1].cget("text") == 'bot' and self.board[i + 2][j - 2].cget("text") == ""):
                                return False

                    except IndexError:
                        pass
            return True

