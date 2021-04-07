# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import codecs

"""
#Поскольку в условии написано "Не програмно" фаил с данными создал руками в блокноте.

# Вариант 1 (Считываем  весь фаил в список)

with codecs.open("zadanie3.txt", "r", "utf-8") as zad3:
    lines = zad3.readlines()  # Создаем список из строк
    i = 0
    zp = 0
    for el in lines:
        i += 1
        words = el.split()
        zp += int(words[1])
        if int(words[1]) < 20000:
            print(f"{words[0]} имеет оклад меньше 20000!")
    sredzp = zp / i
    print(f"Средняя ЗП сотрудников: {sredzp}")
"""

# Вариант 2 ( считываем по строчо)


with codecs.open("zadanie3.txt", "r", "utf-8") as zad3:
    z = 0
    i = 0
    for line in zad3:
            a, b = line.split()  # Считываем строку и разбиваем значения
            z += int(b)  # Подсчитываем сумму окладов
            i += 1  # Считаем колисечтво сотрудников
            if int(b) < 20000:
                print(f"{a} имеет оклад меньше 20000!")

    sredzp = z / i
    print(f"Средняя зп персонала: {sredzp}")


# Вопрос: правильно ли я понимаю, что лучше не считывать весь фаил сразу, а обрабатывать по 1 строке?
# Т.е. Хранит ли питон в памяти все строки которые мы считываем через readline() или каждая новая перезаписываеся?
# Похоже ли это на генератор yeild который хранит одно значение, вместо хранение всего списка?
