'''Натуральные числа. Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К.
Список используемых цифр (прописью) и их количество выводится отдельно.'''

k = 1
a = []
data = []
data_int = []
def ntw(n):
    words = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
    6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return words.get(n)


with open('text.txt') as f:
    file = f.read()
    for i in file.split():
        if i.isdigit():
            data.append((int(i)))

for i in range(len(data)):
    if data[i] % 2 != 0: #проверка на чётность
        if len(str(data[i])) % 2 == 0: #проверка на чётность количества цифр в числе
            if len(str(data[i])) > k: #по условию цифр в числе больше k = 1
                a.append(data[i])
                
print('Исходный список чисел: ', data)
print('Получившийся список: ', a)
if a == []:
    print('Нет подходящих чисел')
for i in a:
    b = ''
    for j in str(i):
        if str(i) not in b:
            if ntw(int(j)) not in b:
                b += ntw(int(j)) + ' '
    print((str(i) + ' - ' + b), 'Количество цифр:', len(str(i)))
