'''Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.'''

class Cell:
    def __init__(self, cells: int):
        self.cells = int(cells)

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells) if (self.cells - other.cells) > 0 else 'Отрицательное число!'

    def __str__(self):
        return f'Результат: {self.cells}'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(round(self.cells / other.cells))

    def make_order(self, data_in_row):
        row = ''
        for itm in range(int(self.cells / data_in_row)):
            row += f'{"*" * data_in_row}\\n'
        row += f'{"*" * (self.cells % data_in_row)}'
        return row

c1 = Cell(7)
c2 = Cell(12)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(5))
print(c2.make_order(7))