# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.


list = [el for el in range(20, 240) if el % 20 == 0]  # Кратные 20
print(list)

list2 = [el for el in range(20, 240) if el % 21 == 0]  # или 21
print(list2)

list3 = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]  #20 или 21
print(list3)