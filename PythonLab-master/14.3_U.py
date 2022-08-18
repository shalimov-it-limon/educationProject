# Функции-генераторы. Задача: выполнить те функции, которые пропиисаны в теле функции.
# ВМЕСТО return - YIELD
# Числа Фибоначчи: f0 = 0, f1 = 1
# Fn = Fn-1 + Fn-2, n >= 2


def fib():
    a, b = 0, 1
    yield a  #F0
    yield b  #F1

    while True:
        a, b = b, a + b
        yield b


for num in fib():
    print(num)
    if num > 10000:
        break


fib_gen = fib()
fib_gen.close()    # Закрытие генератора.

for i in fib_gen:
    print()


fib_gen

def count(start, step):
    counter = start
    while True:
        yield counter
        counter += step


my_gen_func = count(100, 10)
for i in range(10):
    print(next(my_gen_func))


id(my_gen_func) == id(iter(my_gen_func))

# Функция-генератор возвращает бесконечную последовательность натуральных чисел.
# Начало - 1, шаг1. Может быть задано пользоватлем


# def count(start, step):
#     counter = start
#     while True:
#         yield counter
#         counter += step
#
#
# for num in count(5, 2):
#     print(count)

# Генератор цикла: ВхД - массив, [1, 2, 3]. ВыхД - бесконечный возврат 123123123...


# def repeat_list(list_):
#     list_values = list_.copy()
#     while True:
#         value = list_values.pop(0)
#         list_values.append(value)
#         yield value
#
#
# for i in repeat_list([1, 2, 3]):
#     print(i)
#

# Итераторы - (iterator) - объект, который возвращает свли объекты по одному за раз.
# Итератор работает с итерируемыми функциями. Если не известно, итерирема ли функция, подключается
# функция iter(object).
# iter(int)
print(iter([1, 2, 3]))
# Функция next() позволяет получить следующий элемент от итератора.
# МеханизмЖ 1. Получаем итератор от итерируемого объекта, для которого работает итератор.
# 2. Несколько раз обращаемся к итератору и получаем элементы последовательности через next().
for i in range(10):
    pass
    print(i)
print(i)

# Логика итератора: 1. Получаем итератор через iter(iterable_object). 2. Вызываем много раз next(iterator).
# 3. Получаем ошибку Stopiteration, прекращаем работу.
str_ = 'my test'
str_iter = iter(str_)

print(type(str_))   # Строка
print(type(str_iter))   # Итератор строки

print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
# print(next(str_iter))  Stopiteration


def first_gen(input_):
    yield input_
    input_ += 1
    print(input_)


my_first_gen = first_gen(5)
print(next(my_first_gen))
# print(next(my_first_gen))  В строке 94 объявлен только один yield, после него будет Stopiteration


def second_gen(input_):
    yield input_
    input_ += 1

    yield input_
    input_ += 1

    return input_

my_second_gen = second_gen(10)

print(next(my_second_gen))
print(next(my_second_gen))
# print(next(my_second_gen))  Третий принт, потому как yield 2 шт - StopIteration


# def last_gen():
#     for i in range(10):
#         yield i
#         if i == 5:
#             raise StopIteration
#
#
# my_last_gen = last_gen()
#
# for _ in range(10):
#     print(next(my_last_gen))


def my_animal_generator():
    yield 'корова'
    print('----')
    for animal in ['кот', "собака", "медведь"]:
        yield animal
    print('---')
    yield 'кит'


a = my_animal_generator()
print(next(a))

for i in a:
    print(i)

iter((1, 2, 3))
