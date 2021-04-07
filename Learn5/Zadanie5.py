# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("zadanie5.txt", "w") as zad5:
    appstr = input("Введите числа через пробел: ")
    zad5.write(appstr)
with open("zadanie5.txt", "r") as zad5:
    readstr = zad5.read().split()

    print(sum(int(i) for i in readstr))