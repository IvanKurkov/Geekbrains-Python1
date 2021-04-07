# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title="Ручка"):
        super().__init__(title)

    def draw(self):
        print("Возьми меня за ручку!")


class Pencil(Stationery):
    def __init__(self, title="Карандаш"):
        super().__init__(title)

    def draw(self):
        print("Карандаш проглотил?")


class Handle(Stationery):
    def __init__(self, title="Маркер"):
        super().__init__(title)

    def draw(self):
        print("Имея маркер можно закрасить все кроме самого маркера!")


a = Pen()
b = Pencil()
c = Handle()
a.draw()
b.draw()
c.draw()
