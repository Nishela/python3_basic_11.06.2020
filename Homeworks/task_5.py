'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

import random

numbers = [random.randint(1,100) for _ in range(random.randint(1,100))]
summ = sum(numbers)

with open('task_5_data.txt', 'w', encoding='UTF-8') as file:
    str_data = map(str, numbers)
    file.write(' '.join(str_data))

with open('task_5_data.txt', 'r', encoding='UTF-8') as file_2:
    data = file_2.read()
    int_data = map(int, data.split(' '))
    summa = sum(int_data)

print(f'Сумма == {summa}')