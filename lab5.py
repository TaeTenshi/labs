'''
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
Определить (смоделировать) границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме
в виде отчета по лабораторной работе.
16.	F(1) = 1,F(n) = F(n–1) * (n + 1) при четных n > 1 F(n)=n! при нечетных n > 1
'''

from math import factorial
import time
import matplotlib.pyplot as plt

# рекурсивно
def F_rec(n):
    if n == 1:
        return 1
    elif n % 2 == 0 and n > 1:
        return F_rec(n - 1)*(n + 1)
    elif n % 2 != 0 and n > 1:
        return factorial(n)

# итерационно
def F_iter(n):
    if n == 1: # F(1) = 1
        return 1
    elif n % 2 == 0 and n > 1: # F(n) = F(n – 1) * (n + 1)
        for i in range(2, n + 1, 2):
            a = 1
            a *= F_rec(n - 1)*(n + 1)
        return a
    elif n % 2 != 0 and n > 1: # F(n)=n!
        a = 1
        while n > 1:
            a *= n
            n -= 1
        return a

# ввод числа n
n = int(input("Введите число n: "))
while n <= 0:  # ошибка в случае введения не натурального числа
    n = int(input("Введите число больше 0 : "))

recursive_times = []  # таблица
recursive_values = []
iterative_times = []
iterative_values = []
n_values = list(range(1, n + 1, +1))

# подсчёт времени выполнения рекурсивно
start_time = time.time()
f_rec = F_rec(n)
end_time = time.time()
recursive_time = end_time - start_time

# подсчёт времени выполнения итеративно
start_time = time.time()
f_iter = F_iter(n)
end_time = time.time()
iterative_time = end_time - start_time

# заполнение списков
for n in n_values:
    start = time.time()
    recursive_values.append(F_rec(n))
    end = time.time()
    recursive_times.append(end - start)

    start = time.time()
    iterative_values.append(F_iter(n))
    end = time.time()
    iterative_times.append(end - start)

table = []
for i, n in enumerate(n_values):
        table.append([n, recursive_times[i], iterative_times[i], recursive_values[i], iterative_values[i]])
print('{:<10}|{:<22}|{:<22}|{:<25}|{:<30}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)', 'Значение рекурсии', 'Значение итерации')) # вывод таблицы
print('-' * 160)
for j in table:
    print('{:<10}|{:<22}|{:<22}|{:<25}|{:<30}'.format(j[0], j[1], j[2], j[3], j[4]))

# вывод
print("F({}) = {} (рекурсивно в {:.6f} секунд)".format(n, f_rec, recursive_time))
print("F({}) = {} (итеративно в {:.6f} секунд)".format(n, f_iter, iterative_time))

plt.plot([n], [recursive_time], 'ro', label='Рекурсивно')
plt.plot([n], [iterative_time], 'bo', label='Итеративно')
plt.xlabel('n')
plt.ylabel('Время (с)')
plt.title('Сравнение рекурсивного и итерационного подхода')
plt.legend()
plt.show()