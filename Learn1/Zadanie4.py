# Задание 4:  Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения
# используйте цикл while и арифметические операции.

user_number = int(input("Введите число: "))
max_number = 0
while user_number > 0:
    number = user_number % 10
    user_number = user_number // 10
    if number > max_number:
        max_number = number
print(f"Максимальная цифра в числе: {max_number}")

# Забежал на один урок вперед на парралельном курсе, который Вы выложили для ознакомления,
# где рассказывается про списки, и придумал такой вариант

user_number = input("Введите число: ")
numbers = list(user_number)
new_list = sorted(numbers)
print(new_list[-1])

# Потом еще немного подумал и упихал в 2 строки

user_number = input("Введите число: ")
print(sorted(user_number)[-1])
