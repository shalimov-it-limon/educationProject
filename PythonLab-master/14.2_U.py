# Переменные изменяемые и не изменяемые - мутабельные и немутабельные.
# Основоная идея изменяемого типа данных, как аргумента по умолчанию - прописывать в аргументе None, что бы
# каждый раз создавался новый список. def correct_func(name_arg=None):
# Рекурсивная функция - функция, вызывающая сама себя и обрабатывающая данные до момента достижения терминального
# условия (условия остановки). Количество раз, столько функция вызвала сама себя - глубинная рекурсия.
# Чтобы понять рекурсию, надо понять рекурсию.
# Чтобы не уходить в бесконечную рекурсию есть рекрсивный вызов и терминальное условие.
# Факториал числа - это пороизведение натуральных от 1 до самого числа, включая данное число. Обозначение - "!".
# 3! = 1 * 2 * 3
# 1 * 2 * 3 = (1! * 2) * 3 = (2! * 3) = 3! - рекурсивный вызов.
print('Skill GOOD Var')


def fact(n):
   if n == 1:    # терминальное условие.
      return 1
   return n * fact(n - 1)    # рекурсивный вызов.


print(fact(8))

print('My BAD Var')   # РЕКУРСИЯ УШЛА В ЗАКАТ из-за слишком ОГГОМНЫХ данных. Сработала защита.
# def fact(n):
#     if n == 1:    # терминальное условие не сработало! Не может факториал числа быть больше сам себя n + 1
#     или равен сам себе.
#         return 1
#     return n * fact(n + 1)     ! RecursionError: превышена максимальная глубина рекурсии по сравнению !
#     return n * fact(n)         ! RecursionError: превышена максимальная глубина рекурсии по сравнению !
#
# print(fact(8))

# def fact(n):   РЕКУРСИЯ УШЛА В ЗАКАТ из-за слишком ОГГОМНЫХ данных. Сработала защита.
#    if n == 0:    # RecursionError: maximum recursion depth exceeded in comparison
#       return 1
#    return n * fact(n + 1)    # Previous line repeated 995 more times
print(':(')
print('Skill GOOD Var')
# Рекурсия про числа Фибоначчи.
# Терминальное условие F(1) = 1 и F(2) = 2
# Рекурсивная функция F(n) = F(n-1) + F(n-2)
# n - порялковый номер числа Фибоначчи.


def rec_fibb(n):
   if n == 1:
      return 1   # 1-й номер - число 1
   if n == 2:
      return 1   # 2-й номер - число 1, 1 + 1 + ...
   return rec_fibb(n - 1) + rec_fibb(n - 2)


print(rec_fibb(15))

# Функция суммы чисел от 1 до n.
print('My BAD Var')
print(':(')
print('Skill GOOD Var')


def sumer_num(n):
    # sum_ = 0
    if n == -1:
        return -1
    return n + sumer_num(n-1)

print(sumer_num(5))
# Развернуть строку рекурсивной функцией.
print('My BAD Var')
print(':(')
# str_ = input()
#
# def string_backwards(str_):
#
#     if str_[**1::]:
#        return str[::-1]
#
#
# print(string_backwards(**str_))
print('Skill GOOD Var')


def reverse_str(string):
    if len(string) == 0:
        return ''
    else:
        return string[-1] + reverse_str(string[:-1])   # Верни аргумент с полседнего элемента и склей с аргументом
                                                       # в обратном направлении.


print(reverse_str('Люблю грозу в начале мая'))

# Дано натуральное число N. Вычислить сумму его цифр.
print('My BAD Var')
print(':(')
# def summer_n(*num_n):
#     if num_n == 0:
#         return num_n
#     for n in num_n:
#         num_n += n
#         return num_n
#
# print(summer_n(12))
print('Skill GOOD Var')


def sum_digit(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digit(n // 10)


print(sum_digit(12))
