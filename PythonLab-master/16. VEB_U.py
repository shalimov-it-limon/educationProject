import math


def funk1():
    3 + 5


print(funk1())


def funk2():
    return 3 + 5


print(funk2())


def funk3(a, b):
    return a + b


print(funk3(5, 6))

print(funk2() + funk3(4, 6) / 2)
print((funk2() + funk3(4, 6)) / 2)
var1 = funk2()
print(int((var1 + funk3(4, 6)) / 2))
var2 = funk3
print(funk3)
var2 = funk2
print(var2())


def square(x):
    return x * x


print(square(5))
print(math.sqrt(square(5)))
print(math.sqrt(square(5)) + math.pi + funk3(4, 6))
print(math.sqrt(square(funk3(4, 6))))
print(square(funk3(4, 6)))

y = 11 # аргумент
p = 5  # аргумент
q = 6  # аргумент
print(square(y) * funk3(p, q))


def name_age(name, age):
    return f'Меня зовут {name}, мне {age} лет.'


print(name_age('Александр', "15"))
print(name_age(age = 40, name = 'Анна'))


def my_city(name, city='Кемерово'):
    return f'Я, {name}, живу в городе {city}.'


print(my_city('Анна', city='Уфа'))
print(my_city('Анна', 'Бикин'))
print(my_city("Анна"))

18-26