#2. Для списка реализовать обмен значений соседних элементов, т.е.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#При нечетном количестве элементов последний сохранить на своем месте.
#Для заполнения списка элементов необходимо использовать функцию input().




"""
# Ввод элементов списка отдельно
user_list = []
print("Привет, человек! Введи 7 значений в наш список.")
for i in range(7):
    user_list.append(input("Введите элемент: "))
step = 0
for i in range(len(user_list) // 2):
    user_list[step], user_list[step+1] = user_list[step+1], user_list[step]
    step += 2


print(user_list)
"""
"""

# Ввод строки и разбиение на список

user_list = list(input("Введите список: "))

step = 0
for i in range(len(user_list) // 2):
    user_list[step], user_list[step+1] = user_list[step+1], user_list[step]
    step += 2


print(user_list)
"""
"""

# Проба менять не просто две соседние а две соседние на две соседние

user_list = list(input("Введите список: "))

step = 0
for i in range(len(user_list) // 4):
    user_list[step], user_list[step+1], user_list[step+2], user_list[step+3] = user_list[step+3], user_list[step+2], user_list[step], user_list[step+1]
    step += 4

print(user_list)
"""