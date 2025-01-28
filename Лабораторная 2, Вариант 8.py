import math

# Данные
x = -2.235e-2  # x = -2.235 * 10^(-2)
y = 2.23
z = 15.221

# Вычисления
# 1. Числитель
abs_diff = abs(x - y)  # |x - y|
numerator = math.exp(abs_diff) * (abs_diff ** abs(x + y))  # e^{|x-y|} * |x-y|^{|x+y|}

# 2. Знаменатель
denominator = math.atan(x) + math.atan(z)  # arctg(x) + arctg(z)

# 3. Первая часть выражения
first_term = numerator / denominator

# 4. Вторая часть выражения
second_term = (x ** 6 + math.log(y) ** 2) ** (1 / 3)  # кубический корень из (x^6 + ln^2(y))

# Итоговое значение
s = first_term + second_term

# Вывод результата
print(f"s = {s:.4f}")
