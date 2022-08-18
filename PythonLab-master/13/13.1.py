# Операторы и операнды.
# Унарные Операторы - необходимо одно значениие для выполнения действия (унарный минус).
# Бинарные Операторы - необходимы два значениие для выполнения действия.
# Тернарные Операторы- возвращают свой второй или третий операнд в
# зависимости от значения логического выражения, заданного первым операндом.
# ОПЕРАТОРЫ СРАВНЕНИЯ. Результат всегды булево значение.
print(10 < 5)
print(10 > 5)
print(10 <= 5)
print(10 >= 5)
print(10 <= (5 * 2))
print(3 == 5)
print(3 != 5)
print('-' * 50)


print(25 ^ 3)

print('-' * 50)
cond1 = 0 < 1
cond2 = 1 < 4
print(cond1 and cond2)
print('-' * 20)
cond1 = 0 > 1
print(cond1)
cond2 = 1 < 4
print(cond2)
print(cond1 and cond2)
print('-' * 20)
cond1 = 0 > 1
print(cond1)
cond2 = 1 > 4
print(cond2)
print(cond1 and cond2)
print('-' * 20)
name1 = "Ann"  # Регистр имеет значение!
name2 = 'Elen'
cond1 = 'A' in name1
print(cond1)
cond2 = 'A' in name2
print(cond2)
print(cond1 and cond2)
print('-' * 20)
name1 = "Ann"  # Регистр имеет значение!
name2 = 'Elen'
print(not True)
print(not False)
print('-' * 20)