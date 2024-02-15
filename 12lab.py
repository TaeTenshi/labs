"""16. Вычислить сумму знакопеременного ряда (-1)n-1 (|хn|)/(n)!, где х-матрица ранга к (к и матрица задаются случайным образом),
n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой. У алгоритма д.б. линейная сложность."""

import numpy as np

def factorial(n):
    return np.prod(np.arange(1, n + 1, dtype=np.float128))


def calculate_term(x, n, factorial_n):
    rx_n = (x ** n)
    det_x_n = np.linalg.det(x_n)
    return ((det_x_n) / factorial_n) * ((-1) ** (n - 1))


def alternating_series_sum(X, t):
    n = 1
    result = np.zeros_like(X) #возвращает массив нулей той же формы и типа, что и заданный массив.
    term = X.copy()

    while np.any(np.abs(term) >= t):  # проверка на достижение заданной точности для всех элементов
        n += 1
        term = np.matmul(term, X) / n
        result += term if n % 2 == 0 else -term  # Добавление или вычитание терма в зависимости от четности n

    return result


# t как минимальная допустимая точность
k = int(input("Введите ранг матрицы ")) # ввод ранга матрицы
X = np.random.rand(k, k)  # генерация случайной матрицы
t = 1e-6  # требуемая точность
result = alternating_series_sum(X, t)
print(result)
