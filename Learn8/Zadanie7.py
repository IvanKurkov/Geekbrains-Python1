# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class CompNumbers:
    def __init__(self, numb):
        self.numb = complex(numb)

    def __add__(self, other):
        return self.numb + other.numb

    def __mul__(self, other):
        return self.numb * other.numb

    def __str__(self):
        return self.numb


z1 = CompNumbers(1 + 3j)
z2 = CompNumbers(1 - 3j)
print(z2*z1)
print(z2+z1)
z4 = CompNumbers(1 - 3j)
z3 = CompNumbers(1 - 3j)
print(z3*z4)
print(z3+z4)