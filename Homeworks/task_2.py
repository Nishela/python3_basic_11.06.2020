'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def consumption_coat(self):
        return f'Расход ткани на пальто: {self.v / 6.5 + 0.5}'

    def consumption_jacket(self):
        return f'Расход ткани на костюм: {2 * self.h + 0.3}'

    @property
    def total_consumption(self):
        return f'Общий расход ткани: {(self.v / 6.5 + 0.5) + (2 * self.h + 0.3)}'


class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.coat = self.consumption_coat()

    def __str__(self):
        return self.coat

class Jacket(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.jacket = self.consumption_jacket()

    def __str__(self):
        return self.jacket

c = Coat(58,170)
j = Jacket(50,155)
print(c)
print(j)
print(c.total_consumption)
print(j.total_consumption)
print(c.consumption_coat())
print(j.consumption_jacket())