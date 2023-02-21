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
            if buffer >= '0' and buffer <= '9':
                work_buffer += buffer
            buffer = f.read(buffer_len)
        if work_buffer:
            num.append(int(work_buffer))
            if int(work_buffer) % 2 != 0: #проверка на чётность
                if len(str(work_buffer)) % 2 == 0: #проверка на чётность количества цифр в числе
                    if len(str(work_buffer)) > k: #по условию цифр в числе больше k = 1
                        a.append(int(work_buffer))
        work_buffer = ''
        buffer = f.read(buffer_len) #читаем следующий блок

if len(num) == 0:
    print('Чисел нет')
    quit()

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
