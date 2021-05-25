# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Warehouse:
    store = []
    marketing = []

    def __init__(self, direcotry):
        self.directory = direcotry

    @staticmethod
    def acceptinwh(*items):
        """
        Принимаем товар на склад
        :param item: экземпляр предмета
        Добавляем словарь экземпляра в список товаров на складе
        """
        for i, item in enumerate(items):
            Warehouse.store.append(["Склад", (i + 1), item.__dict__])

    @staticmethod
    def acceptnmarketing(*items):
        """
        Записываем данную вещь на маркетинг
        :param item: экземпляр предмета
        Добавляем словарь экземпляра в список товаров в маркетинге
        """
        for i, item in enumerate(items):
            Warehouse.marketing.append(["Маркетинг", (i + 1), item.__dict__])







class OfficeEqp(Warehouse):

    def __init__(self, directory, type, name, coast, val):
        super().__init__(directory)
        """
        directory - раздел на складе
        name - Наименование предмета
        coast - стоимость предмета
        val - количество 
        """
        self.name = name
        self.coast = coast
        self.val = val
        self.type = type


    @classmethod
    def valid_val(cls, _valid):
        while True:
            if str(_valid).isdigit():
                return _valid
            else:
                print(f"Количество должно быть введено в  виде числа!")
                _valid = input("Введите количество верно: ")


class Printer(OfficeEqp):
    def __init__(self, directory, type, name, coast, val, color=False):
        super().__init__(directory, type, name, coast, val)
        """
        directory - раздел на складе
        name - Наименование предмета
        coast - стоимость предмета
        val - количество 
        color - цветной или нет
        """
        self.color = color
        self.val = OfficeEqp.valid_val(val)

class Scanner(OfficeEqp):
    def __init__(self, directory, type, name, coast, val, typescan):
        super().__init__(directory, type, name, coast, val)
        """
         directory - раздел на складе
        name - Наименование предмета
        coast - стоимость предмета
        val - количество 
        type - тип ручной, планшетный или автоподатчик
        """
        self.typescan = typescan


class Copier(OfficeEqp):
    def __init__(self, directory, type, name, coast, val, speed):
        super().__init__(directory, type, name, coast, val)
        """
        directory - раздел на складе
        name - Наименование предмета
        coast - стоимость предмета
        val - количество 
        speed - скорость печати стр в минуту

        """
        self.speed = speed


item1 = Printer("Оффисная техника", "Принтер", "HP-200", 5000, "f", True)

Warehouse.acceptinwh(item1,)

store = Warehouse.store

for i in store:
    print(i)
