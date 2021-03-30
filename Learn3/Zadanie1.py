# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divfn():
    """
    Получаем 2 числа и делим между собой. Если ошибка деления на 0, выдаем сообщение.
    :param var1: Делимое
    :param var2: Делитель
    :return: float
    """
    try:
        return int(input("Введите делимое: ")) / int(input("Введите делитель: "))
    except ZeroDivisionError:
        print("На 0 делить нельзя")


print(divfn())

# Вариант 2

var11 = int(input("Введите делимое: "))
var21 = int(input("Введите делитель: "))


def divfn2(var11, var21):
    """
    Получаем 2 числа и делим между собой. Если ошибка деления на 0, выдаем сообщение.
    :param var11: Делимое
    :param var21: Делитель
    :return: float
    """
    try:
        return var11 / var21
    except ZeroDivisionError:
        print("На 0 делить нельзя")


print(divfn2(var11, var21))