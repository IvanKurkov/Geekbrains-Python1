# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, direcotry):
        self.directory = direcotry

class OfficeEqp(Warehouse):
    def __init__(self, directory, name, coast, val):
        super().__init__(directory)
        self.name = name
        self.coast = coast
        self.val = val

class Printer(OfficeEqp):
    def __init__(self, directory, name, coast, val, color=False):
        super().__init__(directory, name, coast, val)
        """
        color - цветной или нет
        """
        self.color = color

class Scanner(OfficeEqp):
    def __init__(self, directory, name, coast, val, type):
        super().__init__(directory, name, coast, val)
        """
        type - тип ручной, планшетный или автоподатчик
        """
        self.type = type

class Copier(OfficeEqp):
    def __init__(self, directory, name, coast, val, speed):
        super().__init__(directory, name, coast, val)
        """
        speed - скорость печати стр в минуту
        
        """
        self.speed = speed