'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

def my_func(num_1, num_2):
    """
    Фунция принимает 2 аргумента и возвращает результат их деления
    :param num_1: число
    :param num_2: число
    :return: число или строка (при делении на 0)
    """
    try:
        res = num_1 / num_2
    except:
        res = 'Нельзя делить на 0!'
    return res

# цикл проверки первого введенного значения.
while True:
    user_num_1 = input('Введи первое число:\n')
    if user_num_1.isdigit():
        user_num_1 = int(user_num_1)
        break
    else:
        try:
            user_num_1 = float(user_num_1)
            break
        except:
            print('В первой переменной присутствуют буквы!')

# цикл проверки второго введенного значения.
while True:
    user_num_2 = input('Введи второе число:\n')
    if user_num_2.isdigit():
        user_num_2 = int(user_num_2)
        break
    else:
        try:
            user_num_2 = float(user_num_2)
            break
        except:
            print('Во второй переменной присутствуют буквы!')

print(f'Результат деления {user_num_1} на {user_num_2}: {my_func(user_num_1,user_num_2)}')