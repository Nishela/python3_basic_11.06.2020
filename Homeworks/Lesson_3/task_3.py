'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.'''

# Вариант 1: аргументы помещаем в список. В цикле находим наибольший аргумент и удаляем его из списка. Второй аргумент
# находится так же.

def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    while True:
        maximum_1 = max(my_list)
        my_list.remove(maximum_1)
        maximum_2 = max(my_list)
        break
    return maximum_1 + maximum_2

summa = my_func(11,139,9)
print(f'Сумма двух наибольших аргументов == {summa}')

# Вариант 2: аргументы помещаем в список. Находим наименьший аргумент и удаляем его из списка.
# Находим сумму двух оставшихся.
def my_func_2(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.remove(min(my_list))
    return sum(my_list)

summa_2 = my_func_2(11,139,9)
print(f'Сумма двух наибольших аргументов == {summa_2}')

# Вариант 3: Сравниваем элементы друг с другом
def my_func_3(arg_1, arg_2, arg_3):
    if arg_2 <= arg_1 >= arg_3:
        maximum_1 = arg_1
        if arg_2 >= arg_3:
            maximum_2 = arg_2
        summa = maximum_1 + maximum_2
    elif arg_2 > arg_1 > arg_3:
        summa = arg_2 + arg_1
    else:
        arg_2 > arg_1 < arg_3
        summa = arg_2 + arg_3
    return summa

summa_3 = my_func_3(11,139,9)
print(f'Сумма двух наибольших аргументов == {summa_3}')



