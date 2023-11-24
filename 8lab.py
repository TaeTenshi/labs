'''
Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации (л.р. №7)
разработать реализацию с использованием графического интерфейса.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.
'''
import random
import itertools
import tkinter as tk

class Point:
    def __init__(self, x, y):
      self.x = x
      self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


class SquareCalculations:
    def calculate_distance(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        return dx ** 2 + dy ** 2

    def is_square(p1, p2, p3, p4):
        side_length = SquareCalculations.calculate_distance(p1, p2)
        diagonal_length = SquareCalculations.calculate_distance(p1, p3)
        if side_length == 0 or diagonal_length == 0:
            return False
        if SquareCalculations.calculate_distance(p1, p2) == SquareCalculations.calculate_distance(p2, p3) and SquareCalculations.calculate_distance(p2, p3) == SquareCalculations.calculate_distance(
                p3, p4) and SquareCalculations.calculate_distance(p3, p4) == SquareCalculations.calculate_distance(p4, p1):
            if SquareCalculations.calculate_distance(p2, p4) == SquareCalculations.calculate_distance(p1, p3):
                return True
        return False

    def find_squares(points):
      squares = []
      unique_points = list(set(points))
      for p1, p2, p3, p4 in itertools.combinations(unique_points, 4):
          if SquareCalculations.is_square(p1, p2, p3, p4):
              squares.append((p1, p2, p3, p4))
      return squares

    def generate_points(count_points, min_value, max_value):
        check_points = []
        points = []
        while len(points) < count_points:
            x = random.randint(min_value, max_value)
            y = random.randint(min_value, max_value)
            point = Point(x, y)
            if (point.x, point.y) not in check_points:
                check_points.append((point.x, point.y))
                points.append(point)
        return points

    def __init__(self, root):
        self.root = root
        root.geometry("350x350")
        root.title("Square Checker")

        self.point_entries = []
        self.label_min = tk.Label(root, text="Интервал координат от ")
        self.label_min.pack()
        self.min_entry = tk.Entry(root)
        self.min_entry.pack()
        self.label_max = tk.Label(root, text="Интервал координат до ")
        self.label_max.pack()
        self.max_entry = tk.Entry(root)
        self.max_entry.pack()

        self.count_points_label = tk.Label(root, text="Количество точек ")
        self.count_points_label.pack()
        self.count_points_entry = tk.Entry(root)
        self.count_points_entry.pack()

        check_button = tk.Button(root, text="Старт", command=self.start)
        check_button.pack()

        self.answer_label = tk.Label(root, text="")
        self.answer_label.pack()
    def start(self):
        self.min_value = int(self.min_entry.get())
        self.max_value = int(self.max_entry.get())
        self.count_points = int(self.count_points_entry.get())
        points = SquareCalculations.generate_points(self.count_points, self.min_value, self.max_value)
        print('Сгенерированные точки', points)
        squares = SquareCalculations.find_squares(points)
        # результаты
        print("Точки, образующие квадраты:", squares)
        if len(squares) == 0:
            self.answer_label.config(text="Нет квадратов в данном наборе точек.")
        else:
            self.answer_label.config(text=f"Точки, образующие квадраты: \n " + '\n'.join(map(str, squares)))

def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
center_window(root)
app = SquareCalculations(root)
root.mainloop()

