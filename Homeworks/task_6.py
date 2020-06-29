'''6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.'''
import re

res_dict = {}
number = 0
with open('task_6_data.txt') as file:
    data = file.readlines()

for line in data:
    splited = line.split()
    key = splited[0]
    for itm in splited[1:]:
        try:
            value = re.search('\d+', itm)[0]
            number += int(value)
        except:
            pass
    res_dict[key] = number
    number = 0
print(f'Такой получился словарь: {res_dict}')