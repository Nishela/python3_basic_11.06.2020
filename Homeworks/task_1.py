'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

with open('task_1_result.txt', 'w', encoding='UTF-8') as file:
    while True:
        my_str = input('Введ текст:')
        file.write(f'{my_str}\n')
        if my_str == '':
            break