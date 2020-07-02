'''3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).'''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        self.full_name = self.name + ' ' + self.surname
        print(self.full_name)

    def get_total_income(self):
        self.total_income = int(self._income['wage']) + int(self._income['bonus'])
        print(f'Доход с учетом премии состаляет: {self.total_income} р.')

w = Position('Василий', 'Пупкин', 'дворник', 10500, 20000)
w.get_full_name()
print(w.position)
w.get_total_income()
