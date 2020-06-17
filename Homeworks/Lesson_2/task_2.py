'''2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().'''

while True:
    user_str = input('Введи значения:\n')
    if user_str:
        my_list = user_str.split(' ')
        break
    else:
        print('Пусто!')
print(my_list)

for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
print(my_list)


