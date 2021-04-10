# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен
# проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, userdata):
        self.userdata = Data.validdata(userdata)

    @classmethod
    def strinint(cls, userdata):
        return [int(i) for i in userdata.split('-')]

    @staticmethod
    def validdata(userdata):
        valdat = Data.strinint(userdata)
        if valdat[1] > 12:
            print("Месяц указан не верно")
            return None
        elif valdat[2] < 1000:
            print("Давненько это было!")
            return userdata



data1 = Data("1-22-2000")
print(data1.userdata)
data2 = Data("1-12-200")
print(data2.userdata)