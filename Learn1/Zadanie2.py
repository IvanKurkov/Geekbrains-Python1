# Задание 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_seconds = int(input("Введите секунды: "))
hours = 0
minutes = 0
seconds = 0

if user_seconds >= 60:
    minutes = user_seconds // 60
    seconds = user_seconds % 60
    if minutes >= 60:
        hours = minutes // 60
        minutes = minutes % 60
else:
    seconds = user_seconds
print(f"Точное время: {hours}:{minutes}:{seconds}")

