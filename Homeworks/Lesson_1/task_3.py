'''3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''
while True:
    number_1 = input('Введи целое число:\n')
    if number_1.isdigit():
        number_1 = int(number_1)
        break
    else:
        print('Нужно ввести целое число!')
number_2 = int(str(number_1)*2)
number_3 = int(str(number_1)*3)
summ = number_1 + number_2 + number_3
print(f'{number_1} + {number_2} + {number_3} = {summ}')