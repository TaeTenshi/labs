'''
Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода
Вариант 16.
На плоскости задано К точек. Сформировать все возможные варианты выбора множества точек из них на проверку того,
что они принадлежат сторонам квадрата.
'''

from itertools import combinations
import random
import matplotlib.pyplot as plt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def is_on_side(self, side):
        return (self.x == 0 or self.x == side) or (self.y == 0 or self.y == side)

class PointCombos:
    def __init__(self, points):
        self.points = points

    def generate_combos(self):
        valid_combos = []
        for r in range(1, len(self.points) + 1):
            for combo in combinations(self.points, r):
                is_valid = all(point.is_on_side(side) for point in combo)
                if is_valid:
                    valid_combos.append(combo)
        return valid_combos

side = 10  # Длина стороны квадрата
k = 10  # Количество точек

points = []
for i in range(k):
    x = random.randint(0, side)
    y = random.randint(0, side)
    point = Point(x, y)
    print(Point(x, y))
    points.append(point)

point_combos = PointCombos(points)
valid_combos = point_combos.generate_combos()

# Вывод результатов
print(f'Количество точек: {k}')
print(f'Все точки: {points}')
print(f'Количество комбинаций: {len(valid_combos)}')
print('Все комбинации:')
for combo in valid_combos:
    print(combo)

fig, ax = plt.subplots()
x = [point.x for point in points]
y = [point.y for point in points]
ax.scatter(x, y)
plt.show()
