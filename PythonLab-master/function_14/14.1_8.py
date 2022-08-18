import cmath


def sqrt():
    try:
        num = int(input("Enter the number : "))
        if num >= 0:
            main(num)
        else:
            complex_num(num)
    except:
        print("OOPS..!!Something went wrong, try again")
        sqrt()
    return


def main(num):
    square_root = num**(1/2)
    print("The square Root of ", num, " is ", square_root)
    return


def complex_num(num):
    ans = cmath.sqrt(num)
    print("The Square root if ", num, " is ", ans)
    return


sqrt()

# функцию hello_world, которая будет печать приветственную строку "Hello World".
def hello_world(): # My Var
    m = 'hello, world'
    # print(m.replace('h', 'H') and m.replace('w', 'W')) # Неправильно.
    print(m.replace('h', 'H') .replace('w', 'W'))

hello_world()

def hello_world(): # Skill Var
   print("Hello World")

hello_world()

# объявили функцию для подсчета количества символов в неком абстрактном тексте

# def char_frequency(text):
#            text = text.lower()
#            text = text.replace(" ", "")
#            text = text.replace("\n", "")
#
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")
#
# char_frequency()

# Входные данные, которые передаются нашей функции, называются аргументы функции.
# Функция обязана принимать то количество аргументов, которое было объявлено при создании функции.
# Если передать отличное количество аргументов, то функция выдаст ошибку. Рассмотрим на примере.

def pow_func(base):
   print(base ** 2)

pow_func(3)  # 9
pow_func(5)  # 25
pow_func(16)

# Если попытаться вызвать эту функцию без передачи ей аргументов, то вы получите следующую ошибку:
# pow_func()
# # TypeError: pow_func() missing 1 required positional argument: 'base'
# обязательные и необязательные аргументы.
# При вызове функции она должна получить значения всех указанных аргументов при её объявлении.
# Либо эти аргументы будут указаны при вызове, и тогда они являются обязательными.
# Либо вы можете указать значение аргумента, присвоив ему значение по умолчанию.

# функция теперь возводит число в любую степень, но по умолчанию возводит в степень 2.


# функция, которая возводит любое число в степень n
def pow_func(base, n=2):
   print(base ** n)

pow_func(3)  # 9
pow_func(5, 3)  # 125
pow_func(5, 2)

# проверяет, является ли число n делителем числа a. И выводит на экран соответствующее сообщение,
# является ли число делителем или нет.
def del_2(a, n):  # My Var
    if a % n:
        print('YES')
    elif not a % n:
        print('NO')
    else:
        ...

del_2(5, 2)

def check_num(a, n):  # Skill Var
   if a % n == 0:
       print(f"Число {n} является делителем числа {a}")
   else:
       print(f"Число {n} не является делителем числа {a}")

check_num(4, 2)  # Число 2 является делителем числа 4
check_num(5, 2)  # Число 2 не является делителем числа 5

# программу, которая будет печатать лесенку следующего типа:
# N = 5
#
# for i in range(1, N + 1):
#    print("*" * i)

# функцию, которая печатает прямую и «обратную лесенку»:
def back_ladder(n):  # My Var - BAD
    n = 5
    for i in range(1, n + 1):
        print("*" * i)
    n = 5
    for i in range(1, n - 1):
        print("*" * i)
    n = 5
    for i in range(1, n + 1, 2):
        print("*" * i)
    print('-' * 20)
    n = 5
    for i in range(n + 1, 0):
        print("*" * i)
    n = 5
    for i in range(1, n - 1):  # Don't working
        print("*" * i)
    n = 5
    for i in range(1, n + 1, 2):
        print("*" * i)

back_ladder(5)
print('-' * 20)
def back_ladder(n):  # My Var - GOOD
    n = 5
    for i in range(n, 0, -1):
        print("*" * i)
    print('-' * 20)
    n = 5
    for i in range(n, n - 1, -1):
        print("*" * i)
    print('-' * 20)
    n = 5
    for i in range(n, 0, -2):
        print("*" * i)
    print('-' * 20)


back_ladder(5)
print('-' * 20)
def reverse_stair(n):  # Skill Var
   for i in range(n, 0, -1):
       print("*" * i)

reverse_stair(5)