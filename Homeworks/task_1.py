'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''

class Data:
    def __init__(self, data: str):
        self.data = str(data)

    @classmethod
    def data_slicer(cls, data):
        data_list = data.split('-')
        day = int(data_list[0])
        month = int(data_list[1])
        year = int(data_list[2])
        return day, month, year

    @staticmethod
    def validation(day, month, year):
        day_valid = True if 1 <= day <= 31 else f'Некорректный день --> {day}'
        month_valid = True if 1 <= month <= 12 else f'Некорректный месяц --> {month}'
        year_valid = True if 0 <= year <= 2020 else f'Некорректный год --> {year}'

        if day_valid == True and month_valid == True and year_valid == True:
            date = f'{day}-{month}-{year}'
        else:
            date = f'{day_valid}-{month_valid}-{year_valid}\n'
        return date

    def __str__(self):
        return f'Результат:\n{Data.data_slicer(self.data)}'

d = Data('06-07-2020')
print(d)
print(Data.validation(10, 9, 2022))
print(d.validation(18, 14, 2011))
print(Data.data_slicer('06-07-2020'))
print(d.data_slicer('06-07-2020'))
print(Data.validation(2, 10, 2000))