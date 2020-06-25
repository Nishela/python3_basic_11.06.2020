'''5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка'''

from functools import reduce

def my_func(prev_el, el):
    return prev_el * el

user_list = [itm for itm in range(100, 1001) if itm % 2 == 0]
result = reduce(my_func, user_list)
print(f'результат вычисления произведения всех элементов списка: {result}')

