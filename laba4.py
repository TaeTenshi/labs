'''
16. 16.	Формируется матрица F следующим образом: скопировать в нее А и  если в Е максимальный элемент в нечетных столбцах больше, чем сумма чисел в нечетных строках,
то поменять местами С и В симметрично, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A^(-1)*AT – K * F^(-1),
иначе вычисляется выражение (AТ +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
  E B
  D C
'''
import random
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

K = int(input('Введите K: '))
N = int(input('Введите N: '))
if (N % 2 != 0) or ((N / 2) % 2 == 0) or ((N / 2) < 3):
    print('N должно быть четным и чтобы число N/2 было нечетным и больше или равно 3')
    exit()

size = N // 2
A = np.random.randint(-10, 11, (N, N))
print('\nМатрица А:\n', A)
F = A.copy()
print("\nМатрица F\n", F)

E = np.array(A[:size, :size])
print('\nМатрица E:\n', E)
max_E = max(map(max, E[:, 0::2]))
print('Максимальное число в матрице E в нечётных столбцах: ', max_E)
sum_E = sum(map(sum, E[0::2, :]))
print('Cумма чисел в нечетных строках в матрице E: ', sum_E)

C = np.array(A[size + N % 2:N, size + N % 2:N])
B = np.array(A[:size, size + N % 2:N])
print('\nМатрица C:\n', C)
print('\nМатрица B:\n', B)
if max_E > sum_E: # то поменять С и В симметрично
    F[:size, size:] = C[-1::-1, :size]
    F[size:, size:] = B[-1::-1, :size]
    print('Максимальное число в матрице E больше чем сумма чисел в матрице E')
    print('\nИзменённая матрица C:\n', C)
    print('\nИзменённая матрица B:\n', B)
else: # то поменять В и Е несимметрично
    F[:size, size:] = E
    F[:size, :size] = B
    print('Максимальное число в матрице E меньше чем сумма чисел в матрице E')
    print('\n Изменённая матрица F\n', F)

det_A = np.linalg.det(A)
diagonal_F = np.trace(F)
G = np.tril(A) #нижняя треугольная матрица, полученная из А
if det_A > diagonal_F: # то вычисляется выражение A^(-1)*AT – K * F^(-1)
    result = np.linalg.inv(A) * A.transpose() - K * np.linalg.inv(F)
    print('Определитель матрицы А больше суммы диагональных элементов матрицы F, вычисляется выражение A^(-1)*AT – K * F^(-1))')
    print('Результат', result)
else: # то вычисляется выражение (AТ + G - FТ)*K
    result = (A.transpose() + G - F.transpose()) * K
    print('Определитель матрицы А меньше суммы диагональных элементов матрицы F, вычисляется выражение (AТ +G-FТ)*K')
    print('\nРезультат\n', result)
# графики
explode = [0] * (N - 1)
explode.append(0.1)
plt.title("Круговая диаграмма")
try:
    sizes = [round(np.mean(abs(F[i, ::])) * 100, 1) for i in range(N)]
except IndexError:
    sizes = [round(np.mean(abs(F[i, ::])) * 100, 1) for i in range(N)]
plt.pie(sizes, labels=list(range(1, N + 1)), explode=explode, autopct='%1.1f%%', shadow=True)
plt.show()

plt.plot(A)
plt.title("График")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.show()

sns.heatmap(A, cmap="Spectral", annot=True)
plt.title("Тепловая карта")
plt.ylabel("Номер строки")
plt.xlabel("Номер столбца")
plt.show()
