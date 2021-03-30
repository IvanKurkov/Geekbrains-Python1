# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

mylist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, -22, -11]


def myfn4_2(mylist):
    return [mylist[i + 1] for i in range(len(mylist) - 1) if mylist[i + 1] > mylist[i]]


print(myfn4_2(mylist))