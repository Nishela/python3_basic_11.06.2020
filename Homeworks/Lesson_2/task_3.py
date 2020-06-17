'''3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.'''

while True:
    moth = input('Введи месяц:\n')
    if moth.isdigit():
        moth = int(moth)
        if moth <= 12:
            break
        else:
            print('Введи целое число от 1 до 12')
    else:
        print('Введи целое число от 1 до 12')

# Решение через dict
sezon = {'Зима': [1, 2, 12],
         'Весна': [3, 4, 5],
         'Лето': [6, 7, 8],
         'Осень': [9, 10, 11]}
for key in sezon:
    if moth in sezon[key]:
        print(f'В этом месяце - {key}')

# Решение через list
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if moth in winter:
    print('В этом месяце - Зима')
elif moth in spring:
    print('В этом месяце - Весна')
elif moth in summer:
    print('В этом месяце - Лето')
else:
    print('В этом месяце - Осень')