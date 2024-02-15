from tkinter import *
import main

class Programma():
    def __init__(self):
        # window sign in
        self.root = Tk()
        self.root.title("Вход пользователя")
        self.root.geometry('350x250')
        self.root.eval('tk::PlaceWindow . center')

        # логин
        self.label_username = Label(self.root, text="Имя пользователя:")
        self.label_username.pack()
        self.entry_username = Entry(self.root)
        self.entry_username.pack()

        # пароль
        self.label_password = Label(self.root, text="Пароль:")
        self.label_password.pack()
        self.entry_password = Entry(self.root, show="*")
        self.entry_password.pack()

        # Кнопка для входа
        self.login_button = Button(self.root, text="Войти", command=self.log_in)
        self.login_button.pack()

        # кнопка для регистрации
        self.reg_button = Button(self.root, text="Зарегистрироваться", command=self.register)
        self.reg_button.pack()

        # сообщение если неверный логин или нет такого пользователя
        self.label_feedback = Label(self.root)
        self.label_feedback.pack()
        self.root.mainloop()

    def log_in(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.check_user(username, password):
            self.feedback(self.root)

        else:
            self.label_feedback.config(text="Неверное имя пользователя или пароль")

    def register(self):
        self.root.destroy()
        self.root_reg = Tk()
        self.root_reg.title("Регистрация")
        self.root_reg.geometry('350x250')
        self.root_reg.eval('tk::PlaceWindow . center')

        self.label_username = Label(self.root_reg, text="Имя пользователя:")
        self.label_username.pack()
        self.entry_username = Entry(self.root_reg)
        self.entry_username.pack()

        self.label_password = Label(self.root_reg, text="Пароль:")
        self.label_password.pack()
        self.entry_password = Entry(self.root_reg, show="*")
        self.entry_password.pack()
        self.label_feedback = Label(self.root_reg, text="")
        self.label_feedback.pack()

        self.reg_button = Button(self.root_reg, text="Создать аккаунт", command=self.check_acc)
        self.reg_button.pack()

    def check_acc(self):
        username_reg = self.entry_username.get()
        password_reg = self.entry_password.get()

        try:
            with open("Users.txt", mode="r") as users:
                existing_usernames = [line.split(":")[0] for line in users.readlines()]
        except FileNotFoundError:
            open("Users.txt", mode="w").close()

        if username_reg in existing_usernames:
            self.label_feedback.configure(text="Этот логин уже занят")
        else:
            with open("Users.txt", mode="a") as users:
                users.write(f"{username_reg}:{password_reg}\n")
            self.feedback(self.root_reg)

    def feedback(self, root_to_close):
        root_to_close.destroy()
        root = Tk()
        main.RussianCheckers(root)


    def check_user(self, username, password):
        try:
            with open("Users.txt", "r") as file:
                users = file.readlines()
                users = [user.strip() for user in users]

                for user in users:
                    user_data = user.split(":")
                    if user_data[0] == username and user_data[1] == password:
                        return True

            return False
        except FileNotFoundError:
            return False

    # def on_validate(self, empty_label):
    #     if empty_label.strip() == "":
    #         return False
    #     return True

program = Programma()