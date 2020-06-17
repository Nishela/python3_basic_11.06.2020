'''4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.'''
while True:
    number = input('Введи целое положительное число:\n')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('Нужно ввести целое положительное число!')

result = 0
while number and result != 9:
    new_num = number % 10
    print(new_num)
    if new_num > result:
        result = new_num
    number//=10
print(result)

result = 9

while number:
    if str(result) in str(number):
        print(result)
        break
    else:
        result -= 1