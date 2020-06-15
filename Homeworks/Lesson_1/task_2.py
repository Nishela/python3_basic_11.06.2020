'''2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.'''

while True:
    total_time_sec = input('Введите время в секундах:\n')
    if total_time_sec.isdigit():
        total_time_sec = int(total_time_sec)
        break
    else:
        print('Вводить только цифры!')

hours = int(total_time_sec / 3600)
minutes = int((total_time_sec / 60) % 60)
seconds = total_time_sec % 60
# если начение не двухзначное, то добавляем 0 в начало
if hours <= 9: # <= 9 можно заменить на in range(10)
    hours = '0' + str(hours)

if minutes <= 9: # <= 9 можно заменить на in range(10)
    minutes = '0' + str(minutes)

if seconds <= 9: # <= 9 можно заменить на in range(10)
    seconds = '0' + str(seconds)
print(f'\nВремя: {hours}:{minutes}:{seconds}')