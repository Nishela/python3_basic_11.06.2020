'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''
from functools import reduce

def summator(prev_el, el):
    return float(prev_el) + float(el)

with open('task_5_data.txt') as file:
    numbers = file.read().split(' ')

summa = reduce(summator, numbers)
print(f'Сумма чисел == {summa}')