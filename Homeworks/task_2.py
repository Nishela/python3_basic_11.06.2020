'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''

class ZeroDiv(Exception):
    def __init__(self, text):
        self.text = text

while True:
    user_divide = input('Введи делимое:\n')
    user_division = input('Введи делитель:\n')
    try:
        if int(user_division) == 0:
            raise ZeroDiv('А-ТА-ТА!!! Деление на 0!!!')
        data = int(user_divide) / int(user_division)
    except ZeroDiv as err:
        print(err)
    else:
        print(f'Результат: {int(data)}')


