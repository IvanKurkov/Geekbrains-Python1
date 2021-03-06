# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.



def my_func(x, y):
    """
    Просто возводим X в степень Y. Даже отрицательная степень нормально возводится
    :param x: int
    :param y: int
    :return:
    """
    return x ** y


print(my_func(2, -3))


def my_func2(x, y):
    """
    Создаем цикл For с функцией Range, где Range равно модуль Y - 1. Определяем начальное число z = x
    Каждый цикл умножает z на x.
    Далее возвращаем 1 / x что бы возвести в отриц степень.
    :param x: int
    :param y: int
    :return:
    """
    z = x
    for i in range(abs(y)-1):
        z *= x
    return 1 / z

print(my_func2(2, -3))