# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.


class Warehouse:
    """
    Так как ни как не оговаривается, как должно выглядеть другое подразделение, использую просто список.
    """
    store = []  # Список добра на складе.
    marketing = []  # Типа список добра в подразделении.

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


item1 = Printer("Оффисная техника", "Принтер", "HP-200", 5000, 1, True)
item2 = Scanner("Оффисная техника", "Сканнер", "Zebra 2323", 5000, 1, "Handle")
item3 = Copier("Оффисная техника", "Копир", "Canon 500", 5000, 1, 20)
item4 = Printer("Оффисная техника", "Принтер", "Kyocera 4332", 5000, 1, True)
Warehouse.acceptinwh(item1, item2, item3)
Warehouse.acceptnmarketing(item4)
store = Warehouse.store
marketing = Warehouse.marketing
# print(store)
for i in store:
    print(i)
for i in marketing:
    print(i)
