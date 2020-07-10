'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.'''

class Store:
    my_store = {}
    _printers = []
    _scanners = []
    _copiers = []

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Printer(Store):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)
        if super()._printers != []:
            for itm in super()._printers:
                if self.name == itm[0] and self.price == itm[2]:
                    itm[1] += self.quantity
                else:
                    super()._printers.append([self.name, self.quantity, self.price])
        else:
            super()._printers.append([self.name, self.quantity, self.price])
        super().my_store.update({'Принтеры': super()._printers})

    def stamp(self):
        return f'Принтеры фирмы "{self.name}" умеют печатать!'

class Scanner(Store):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)
        if super()._scanners != []:
            for itm in super()._scanners:
                if self.name == itm[0] and self.price == itm[2]:
                    itm[1] += self.quantity
                else:
                    super()._scanners.append([self.name, self.quantity, self.price])
        else:
            super()._scanners.append([self.name, self.quantity, self.price])
        super().my_store.update({'Сканеры': super()._scanners})

    def scan(self):
        return f'Сканеры фирмы "{self.name}" делают качественные сканы!'

class Xerox(Store):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)
        if super()._copiers != []:
            for itm in super()._copiers:
                if self.name == itm[0] and self.price == itm[2]:
                    itm[1] += self.quantity
                else:
                    super()._copiers.append([self.name, self.quantity, self.price])
        else:
            super()._copiers.append([self.name, self.quantity, self.price])
        super().my_store.update({'Сканеры': super()._copiers})

    def copy(self):
        return f'Ксероксы фирмы "{self.name}" делают качественные копии!'

class CantInt(Exception):
    def __init__(self, text):
        self.text = text

if __name__ == '__main__':
    print('='*15 + ' Проект "СКЛАД" ' + '='*15)
    while True:
        user_info = input('Что привезли?\n1 = Принтеры\n2 = Сканеры\n3 = Ксероксы\nQ = Выход\n>>> ')
        if user_info == 'Q':
            print(f'На складе есть: {Store.my_store}')
            break
        if user_info:
            data = input('Введи марку, количество, цену за ед.:\n')
            try:
                if not data.split(',')[1].isdigit():
                    raise CantInt('Error!!!\nКоличество HW не целое число!\n')
                hw_name, hw_quantity, hw_price = data.split(',')[0], int(data.split(',')[1]), data.split(',')[2]
                if user_info == '1':
                    hw = Printer(hw_name, hw_quantity, hw_price)
                    print(hw.stamp())
                elif user_info == '2':
                    hw = Scanner(hw_name, hw_quantity, hw_price)
                    print(hw.scan())
                elif user_info == '3':
                    hw = Xerox(hw_name, hw_quantity, hw_price)
                    print(hw.copy())
            except CantInt as err:
                print(err)