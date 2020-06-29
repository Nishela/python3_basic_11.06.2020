'''Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''
import re

words_dic = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('task_4_data.txt') as file, open('task_4_result.txt', 'w', encoding='UTF-8') as file_2:
    quantity = len(file.readlines())
    file.seek(0)
    while quantity > 0:
        data = file.readline()
        quantity -= 1
        key_word = re.search('\w+', data)[0]
        if key_word in words_dic:
            data = re.sub(key_word, words_dic[key_word], data)
            print(data, end='')
            file_2.write(data)