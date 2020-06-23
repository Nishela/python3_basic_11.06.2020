'''4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.'''

# Вариант 1: **
def my_func(x, y):
    return x ** y

# Вариант 2: реализация через цикл
def my_func_2(x, y):
    z = 1
    while y < 0:
        z *= x
        y += 1
    return 1 / z

while True:
    x = input('Введи x:\n')
    if x[0] == '-':
        print('Некорректный ввод!')
    elif x[0].isdigit():
        try:
            x = int(x)
            break
        except:
            try:
                x = float(x)
                break
            except:
                print('Некорректный ввод!')
    else:
        print('Некорректный ввод!')

while True:
    y = input('Введи y:\n')
    if y[0] == '-' and y[1].isdigit():
        try:
            y = int(y)
            break
        except:
            print('Некорректный ввод!')
    else:
        print('Некорректный ввод!')

if x and y:
    print(f'Вариант 1: через ** {my_func.__name__}\nX в степени Y == {my_func(x, y):.3}')
    print(f'Вариант 2: через цикл {my_func_2.__name__}\nX в степени Y == {my_func_2(x, y):.3}')