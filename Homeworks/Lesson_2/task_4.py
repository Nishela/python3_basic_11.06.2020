'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.'''

while True:
    user_str = input('Введи строку:\n')
    if len(user_str) > 0:
        break
    else:
        print('Строка не должна быть пустой!')
user_list = user_str.split(' ')
for index, value in enumerate(user_list, 1):
    print(index, value[:11])