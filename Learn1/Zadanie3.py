# Задание 3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = int(input("Введите число: "))
answer = user_number + int(str(user_number) + str(user_number)) + int(str(user_number) + str(user_number) + str(user_number))
print(answer)

# Или так

user_number = int(input("Введите число: "))
answer = user_number + int(str(user_number) * 2) + int(str(user_number) * 3)
print(answer)
