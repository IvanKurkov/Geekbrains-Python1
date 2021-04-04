# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
# премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

# class Worker:
#     name = "Василий"
#     surname = "Петров"
#     positions = "Уборщик"
#     _income = {"wage": 15000, "bonus": 5000}
# class Positions(Worker):
#     def

class Worker:
    mans = 0
    def __init__(self, name, surname, positions, wage, bonus):
        self.name = name
        self.surname = surname
        self.positions = positions
        self._income = {"wage": wage, "bonus": bonus}
        Worker.mans += 1

class Positions(Worker):
    def __init__(self, name, surname, positions, wage, bonus):
        super().__init__(name, surname, positions, wage, bonus)
    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.surname} {self.name}")

    def get_total_income(self):
        print(f"Доход сотрудника: {int(self._income['wage']) + int(self._income['bonus'])}")


man = Positions("Василий", "Петров", "Уборщик", 15000, 5000)
print(man.mans)
man.get_full_name()
man.get_total_income()


man2 = Positions("Юрий", "Гагарин", "Космонавт", 1504500, 660000)
print(man.mans)
man2.get_full_name()
man2.get_total_income()
