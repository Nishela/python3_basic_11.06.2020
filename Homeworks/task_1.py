'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.'''

class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.matrix = [[0 for _ in range(len(self.list1[i]))] for i in range(len(self.list2))]

    def __add__(self):
        for i in range(len(self.list1)):
            for j in range(len(self.list2[i])):
                self.matrix[i][j] = self.list1[i][j] + self.list2[i][j]
        return '\n'.join(['\t'.join(str(j) for j in itm) for itm in self.matrix])

    def __str__(self):
        return '\n'.join(['\t'.join(str(j) for j in itm) for itm in self.matrix])


matrix = Matrix([[10,2,43],
                 [51,31,5]],
                [[3,19,22],
                 [5,4,16]])

print(f'Результат сложения 2х матриц:\n{matrix.__add__()}')
