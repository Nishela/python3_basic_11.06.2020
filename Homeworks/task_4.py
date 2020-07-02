'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала!\n')

    def stop(self):
        print(f'Машина {self.name} остановилась!\n')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}\n')

    def showspeed(self):
        print(f'Текущая скорость машины {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def showspeed(self):
        if self.speed > 60:
            print(f'{self.name} Превышение скорости!!! --> {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.name}: {self.speed} км/ч')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def showspeed(self):
        if self.speed > 40:
            print(f'{self.name} Превышение скорости!!! --> {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.name}: {self.speed} км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

if __name__ == '__main__':
    town = TownCar(61, 'Белый', 'VW', False)
    work = WorkCar(43, 'Черный', 'Газель', False)
    sport = SportCar(200, 'Красный', 'Porshe', False)
    police = PoliceCar(90, 'Синий', 'Skoda', True)


