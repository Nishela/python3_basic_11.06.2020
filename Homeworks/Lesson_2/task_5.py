'''5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.'''

my_list = [7, 5, 3, 3, 2]
while True:
    user_number = input('Введи натуральное число:\n')
    if user_number.isdigit():
        user_number = int(user_number)
        break
    else:
        print('Нужно ввести натуральное число!')

for i in my_list:
    if user_number in my_list:
        index = my_list.index(user_number)
        if i == user_number and my_list.index(i) > index:
            index += 1
        else:
            my_list.insert(index, user_number)
            break
    else:
        if user_number > i:
            index = my_list.index(i)
            my_list.insert(index, user_number)
            break
        else:
            my_list.append(user_number)
            break
print(f'Пользователь ввел число: {user_number}. Результат: {my_list}')
