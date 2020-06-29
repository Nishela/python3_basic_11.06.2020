'''2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.'''

with open('task_2_data.txt', 'r', encoding='UTF-8') as file:
    list_str = file.readlines()
    quantity = len(list_str)
    if quantity > 4:
        print(f'В документе {quantity} строк')
    elif 5 > quantity > 1:
        print(f'В документе {quantity} строки')
    else:
        print(f'В документе {quantity} строка')
    for count, line in enumerate(list_str, 1):
        words = line.split()
        word_number = len(words)
        if word_number == 1:
            print(f'В {count}-й строке {word_number} слово')
        elif 5 > word_number > 1:
            print(f'В {count}-й строке {word_number} слова')
        else:
            print(f'В {count}-й строке {word_number} слов')
