# Дано целое число 123456789. Определите, входит ли в него цифра 5.
print(5 in 123456789)
a = 12346789
a1 = list(str(a))
print(a1)
print('5' in a1) # Мой вариант самый-самый.
print('5' in str(12346789))
print('-' * 20)
n = 123456789
n = list(str(123456789))
# print(a)
print(list(map(int, n)))
print("5" in list(n))
list_digit = list(map(int, list(str(123456789))))
print(5 in list_digit)
print('-' * 50)

# Дано n-значное целое число N. Определите, входят ли в него цифры 3 и 7.
N = input('Число: ')
# print(str(3) or str(7) in N)
print(str(3) and str(7) in N) # Мой вариант.
print(str(3) in N)
print(str(7) in N)
print('3' in str(N) and '7' in str(N)) # Вариант платформы.
print('-' * 50)

a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
print(a == b)
print(a is b)
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a == b)
print(a is b)
# None используется, например, когда мы не знаем значение переменной, но хотим объявить её.
a = None
print(type(a))