import random
import itertools


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

    def generate_points(n, min_value, max_value):
        check_points = []
        points = []
        while len(points) < n:
            x = random.randint(min_value, max_value)
            y = random.randint(min_value, max_value)
            point = Point(x, y)
            if (point.x, point.y) not in check_points:
                check_points.append((point.x, point.y))
                points.append(point)
        return points


# ввод диапазона генерации точек и количества точек
min_value = 0  # int(input("Введите минимальное значение для координат: "))
max_value = 3  # int(input("Введите максимальное значение для координат: "))
n = 10  # int(input("Введите количество точек: "))

# генерация точек и поиск квадратов
points = SquareCalculations.generate_points(n, min_value, max_value)
print('Сгенерированные точки', points)
squares = SquareCalculations.find_squares(points)

# результаты
print("Точки, образующие квадраты:")
if len(squares) == 0:
    print("Нет квадратов в данном наборе точек.")
else:
    for square in squares:
        print(square)
