'''Натуральные числа. Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К.
Список используемых цифр (прописью) и их количество выводится отдельно.'''

k = 1
a = []
data = []
num = []
def ntw(n):
    words = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
    6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return words.get(n)

with open('text.txt') as f:
    file = f.read()
    for i in file.split():
        data.append(i)

for i in data:
    h = 0
    for j in range(len(i)):
        if h > 0:
            h -= 1
            break
        else:
            if i[j].isdigit():
                number = i[j]
                h = 1
                while True:
                    try:
                        if i[j + h].isdigit():
                            number += i[j + h]
                        if i[j + h].isdigit() == False:
                            break
                        h += 1
                    except IndexError:
                        break
                num.append(int(number))

if len(num) == 0:
    print('цифр нет')
    quit()

for i in range(len(num)):
    if num[i] % 2 != 0: #проверка на чётность
        if len(str(num[i])) % 2 == 0: #проверка на чётность количества цифр в числе
            if len(str(num[i])) > k: #по условию цифр в числе больше k = 1
                a.append(num[i])
print('Исходный список:', data)                
print('Исходный список чисел: ', num)
print('Cписок чисел подходящие под условия: ', a)
if a == []:
    print('Нет подходящих чисел')
    
for i in a:
    b = ''
    for j in str(i):
        if str(i) not in b:
            if ntw(int(j)) not in b:
                b += ntw(int(j)) + ' '
    print((str(i) + ' - ' + b), 'Количество цифр:', len(str(i)))
