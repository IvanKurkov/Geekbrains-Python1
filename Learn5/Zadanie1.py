# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

import codecs

with codecs.open("zadanie1.txt", "a", "utf-8") as zad1:
    while True:  # Делаем бесконечный цикл, чтобы пользователь вводил скоько угодно строк, которые будем записывать.
        appfile = input("Введите строку: ")
        zad1.write(f"{appfile}\n")
        if not appfile:  # Об окончании ввода данных свидетельствует пустая строка.
            break