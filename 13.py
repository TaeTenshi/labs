"""16.	Определить количество детей(<18)  , севших в порту Квинстаун, в возрастном интервале мода +- 10 позиций и сколько из них выжило"""
import csv

filename = "titanic.csv"
children = []

with open(filename, 'r', newline='', encoding='utf-8') as file:
    file_reader = csv.DictReader(file)
    for row in file_reader:
        if row['Age']:
            if row['Embarked'] == 'Q' and float(row['Age']) < 18 and row['Survived'] != '':
                children.append([float(row['Age']), row['Survived'] == '1'])
sort_children = sorted(children, key=lambda child: child[0])

median_children = None
if len(sort_children) <= 21: # 21 - количество чисел с медианой +- 10
    median_children = sort_children
else:
    n = len(sort_children)
    index = n // 2
    if n % 2 != 0:
        median_children = sort_children[index - 10: index + 10]
    else:
        median_children = sort_children[index - 10: index + 11]
survived = 0
for child in median_children:
    if child[1]:
        survived += 1
print(f'Количество  детей, севших в порту Квинстаут : {len(median_children)}')
print(f'Из них выжило : {survived}')