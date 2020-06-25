'''7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.'''
from functools import reduce

def fact(n):
    for itm in range(1, n+1):
        yield itm

def my_func(prev_el, el):
    return prev_el * el

user_input = input('Введи целое число: \n')
user_input = int(user_input)
my_list = [el for el in fact(user_input)]

for el in fact(user_input):
    print(f'{el}!', end=' ')

factorial = reduce(my_func, my_list)
print(f'\nФакториал {user_input}! == {factorial}')
