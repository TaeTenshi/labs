'''Натуральные числа. Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К.
Список используемых цифр (прописью) и их количество выводится отдельно.'''

k = 1
a = []
data = []
num = []
buffer_len = 1
work_buffer = ''

def ntw(n):
    words = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
    6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return words.get(n)

with open('text.txt','r') as f:
    buffer=f.read(buffer_len) #читаем первый блок
    if not buffer: 
        print('Файл пустой')
    while buffer: #обрабатываем текущий блок
        while buffer >= '0' and buffer <= '9':
            work_buffer += buffer
            buffer=f.read(buffer_len)
        if work_buffer:
            kn = 0
            pn = 0
            for j in range(len(work_buffer)):
                try:
                    if work_buffer[j] == '0':
                        kn += 1
                        if kn == 5:
                            pn += 1
                            kn = 0
                    elif work_buffer[j] != '0':
                        kn = 0
                except IndexError:
                    break
            if pn in [0, 2]:
                num.append(work_buffer)
        work_buffer = ''
        buffer = f.read(buffer_len) #читаем следующий блок
        
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
    print('Чисел нет')
    quit()

for i in num:
    indx = num.index(i)
    num[indx] = int(i)
    
for i in range(len(num)):
    if num[i] % 2 != 0: #проверка на чётность
        if len(str(num[i])) % 2 == 0: #проверка на чётность количества цифр в числе
            if len(str(num[i])) > k: #по условию цифр в числе больше k = 1
                a.append(num[i])               
print('Исходный список чисел: ', num)
print('Cписок чисел подходящие под условия: ', a)
if a == []:
    print('Нет подходящих под условия чисел')
    
for i in a:
    b = ''
    for j in str(i):
        if str(i) not in b:
            if ntw(int(j)) not in b:
                b += ntw(int(j)) + ' '
    print((str(i) + ' - ' + b), 'Количество цифр:', len(str(i)))
