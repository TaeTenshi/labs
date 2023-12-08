import tkinter as tk


class Programma():
    open("Users.txt", "w").close()

    def __init__(self):
        # window sign in
        self.root = tk.Tk()
        self.root.title("Вход пользователя")
        self.root.geometry('350x250')
        self.root.eval('tk::PlaceWindow . center')

        # логин
        self.label_username = tk.Label(self.root, text="Имя пользователя:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack()

        # пароль
        self.label_password = tk.Label(self.root, text="Пароль:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        # Кнопка для входа
        self.login_button = tk.Button(self.root, text="Войти", command=self.log_in)
        self.login_button.pack()

        # кнопка для регистрации
        self.reg_button = tk.Button(self.root, text="Зарегистрироваться", command=self.register)
        self.reg_button.pack()

        # сообщение если неверный логин или нет такого пользователя
        self.label_feedback = tk.Label(self.root)
        self.label_feedback.pack()
        self.root.mainloop()

    def log_in(self):
        username = self.entry_username.get().strip()  

        if " " in username:  # Проверяем наличие пробелов в логине
            self.label_feedback.config(text="Логин не может содержать пробелы")
            return

        password = self.entry_password.get()

        if self.check_user(username, password):
            self.feedback(self.root)
        else:
            self.label_feedback.config(text="Неверное имя пользователя или пароль")

    def register(self):
        self.root.withdraw()
        self.root_reg = tk.Tk()
        self.root_reg.title("Регистрация")
        self.root_reg.geometry('350x250')
        self.root_reg.eval('tk::PlaceWindow . center')


        self.label_username = tk.Label(self.root_reg, text="Имя пользователя:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self.root_reg)
        self.entry_username.pack()

        self.label_password = tk.Label(self.root_reg, text="Пароль:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.root_reg, show="*")
        self.entry_password.pack()

        self.reg_button = tk.Button(self.root_reg, text="Создать аккаунт", command=self.check_acc)
        self.reg_button.pack()

        self.label_feedback = tk.Label(self.root_reg, text="")
        self.label_feedback.pack()
    def check_acc(self):
        username_reg = self.entry_username.get().strip()  # удаляем пробелы в начале и в конце
        password_reg = self.entry_password.get()

        with open("Users.txt", mode="r") as users:
            existing_usernames = [line.split(":")[0] for line in users.readlines()]

        if " " in username_reg:
            self.label_feedback.config(text="Логин не может содержать пробелы")
        elif username_reg in existing_usernames:
            self.label_feedback.config(text="Этот логин уже занят")
        elif username_reg == "" or password_reg == "":
            self.label_feedback.config(text="Поле не может быть пустым")
        elif " " in password_reg:
            self.label_feedback.config(text="Пароль не может содержать пробелы")
        else:
            with open("Users.txt", mode="a") as users:
                users.write(f"{username_reg}:{password_reg}\n")
            self.feedback(self.root_reg)

    def feedback(self, root_to_close):
        root_to_close.destroy()
        self.root_feedback = tk.Tk()
        self.root_feedback.eval('tk::PlaceWindow . center')
        self.root_feedback.title("Обратная связь")
        self.label_password = tk.Label(self.root_feedback, text="Вы успешно авторизовались")
        self.label_password.pack()
        self.root_feedback.mainloop()

    def check_user(self, username, password):
        with open("Users.txt", "r") as file:
            users = file.readlines()
            users = [user.strip() for user in users]

            for user in users:
                user_data = user.split(":")
                if user_data[0] == username and user_data[1] == password and user_data[0] != "":
                    return True
                else:
                    return False


program = Programma()
