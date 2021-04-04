# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Скорость {self.name}: {self.speed}")

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, where):
        self.where = where
        if self.where == "l":
            print(f"Машина {self.name} повернула на лево")
        elif self.where == "r":
            print(f"Машина {self.name} повернула на право")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость {self.name}: превышена!")
        else:
            print(f"Скорость {self.name}: {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость {self.name}: превышена!")
        else:
            print(f"Скорость {self.name}: {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


a = TownCar(65, "Red", "Mazda")
b = SportCar(80, "White", "Ferrari")
c = WorkCar(90, "Blue", "Oka")
d = PoliceCar(79, "White-Blue", "Lada9")
a.stop()
b.go()
c.turn("l")
d.turn("r")
a.show_speed()
b.show_speed()
c.show_speed()
d.show_speed()
print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
print(d.__dict__)