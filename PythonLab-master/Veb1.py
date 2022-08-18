#
# Неизменяемые - Строки, числа, кортежи, булевые значения.
# Изменяемые - множества, списки, словари.
index_of_array = 1
value = int(input())
print(type(value))
value1 = float(input())
print(type(value1))
print(value1 ** value)

value = 'Hello, world'

for i in range(len(value)):
    print(value[i])
num1 = num2 = 5
print(num1, num2)
num1, num2 = 5, 7
print(num1, num2)

swap1 = 8
swap2 = 9
swap1, swap2 = swap2, swap1 # Обмен аргументов.
print(swap1, swap2)
swap2 = swap2 - num1
print(swap2)
*z, x, c = [1, 2, 3, 4, 5, 6] # Символ * (арк) заключает в список значения.
print(z)
print(x)
print(c)
x = input('ВВод ')
print(type(x))
g = float(x) + 5.5
print(int(g))
if True:
    print('if')
if True:
    print('elif')
if True:
    print('else')
print(4 == 5)
print(6 == 6)
print(4 != 5)
x = 0
if x == 0:
    print('OK')
elif x != 0:
    print('Non')
else:
    print('Yeah')

x = [1, 4]

if x == 0:
    x = 1
    print('x был равен нулю.')
elif type(x) == type (5) or type(x) == type (5.5):
    print('x - допустимое значение')
else:
    print('x - недопустимый тип данных.')
    x = 1

print(100 / x)