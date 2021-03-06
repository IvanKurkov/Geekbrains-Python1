# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re, codecs

goal = {}
with codecs.open("Zadanie6.txt", "r", "utf-8") as zad6:
    for line in zad6:
        a, *b = line.split()
        nums = [int(i) for i in re.findall(r'\d+', "".join(b))]  # Получаем числа из строки которые потом сложим
        # (Может есть правильнее способ получить числа из подобной строки?)
        goal[a.strip(":")] = sum(nums)

print(goal)
