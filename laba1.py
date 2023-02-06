import random

k = 1
a = []
def ntw(n):
    words = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
    6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return words.get(n)
output_str = " "
list_num = []

#l = [random.randint(1, 10000) for i in range(10)]
list = [1, 20, 300, 455, 557, 6666, 7777]
for i in range(len(list)):
    if list[i] % 2 != 0: #проверка на чётность
        if len(str(list[i])) % 2 == 0: #проверка на чётность количества цифр в числе
            if len(str(list[i])) > k: #по условию цифр в числе больше k = 2
                print(i)
                a.append(list[i])
print(list)
print(a)
for i in a:
    b = ''
    for j in str(i):
        b += ntw(int(j)) + ' '
    print((str(i) + ' ' + b), len(str(i)))

