'''2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.'''
import re

def about_user(first_name, last_name, year, city, e_mail, phone):
    return f'Имя: {first_name} \\ Фамиллия: {last_name} \\ Год рождения: {year} \\ Город: {city} \\ E-mail: {e_mail} \\ Тел.: {phone}'

while True:
    while True:
        user_name = input('Введи имя:\n')
        # Т.к. имя может состоять только из букв, то исключаем присутствие других символов в имени
        user_name_checked = user_name if user_name.isalpha() else False
        if not user_name_checked:
            print('Некорректный формат имени!\n')
        else:
            break


    while True:
        user_l_name = input('Введи фамилию:\n')
        # Т.к. фамилия может состоять только из букв, то исключаем присутствие других символов в фамилии
        l_name_template = '([A-я]+-[A-я]+)|([A-я]+)'
        check = re.search(l_name_template, user_l_name)
        l_name_checked = user_l_name if check[0] == user_l_name else False
        if not l_name_checked:
            print('Некорректный формат фамилии!\n')
        else:
            break

    while True:
        user_year = input('Введи год рождения:\n')
        # Т.к. год может быть только целым числом не больше текущего года, то исключаем присутствие других символов
        year_checked = int(user_year) if user_year.isdigit() else False
        if not year_checked or year_checked > 2020:
            print('Некорректный год!\n')
        else:
            break

    # запрос контактной информации реализован в отдельном цикле
    while True:
        user_city = input('Введи город:\n')
        city_template = '([A-я]+-[A-я]+)|([A-я]+\s{1}[A-я]+\s{1}[A-я]+)|([A-я]+-[0-9]{3})|([A-я]+)'
        check = re.search(city_template, user_city)
        city_checked = user_city if check[0] == user_city else False
        # в городе не могут присутствовать цифры и символы кроме -
        if not city_checked:
            print('Некорректный формат!\n')
        else:
            break

    while True:
        user_email = input('Введи E-mail:\n')
        # email должен быть в формате: имя@домен.ru или com. Для проверки используем регулярные выражения
        email_checked = user_email if re.search('\w+@\w+\.ru|com', user_email) else False
        if not email_checked:
            print('Некорректный домен! (abc@domen.ru | abc@domen.com)\n')
        else:
            break

    while True:
        user_phone = input('Введи номер телефона +7(012)345-67-89:\n')
        phone_checked = user_phone if re.search('\+\d+[(]\d+[)]\d+-\d+-\d+', user_phone) else False
        if not phone_checked:
            print('Некорректный формат! +7(012)345-67-89:\n')
        else:
            break
    break

if True:
    info = about_user(first_name=user_name_checked, last_name=user_l_name, year=year_checked,
                      city=city_checked, e_mail=email_checked, phone=phone_checked)
    print(info)