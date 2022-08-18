# Функции умеют не только принимать аргументы, необходимые для их выполнения,
# но и возвращать значения.
# Делается это с помощью ключевого слова return.
def pow_func(base, n=2):
   print(base ** n)

print(pow_func(3))
# 9
# None
def pow_func(base, n=2):
   print(base ** n)

pow_func(3)  # 9

# функции всегда что-то возвращают, и если этого не указали,
# то автоматически интерпретатор подставит строку return None в конец функции.
def pow_func(base, n=2):
   print(base ** n)
   return None

print(pow_func(3))

print('My Var')
def pow_func(base, n=2):
   print(base ** n)
   return (base ** n)

print(pow_func(3))

print('Skill Var')
def pow_func(base, n=2):
   inside_result = base ** n
   return inside_result


print(pow_func(3))

# можем присвоить этот результат некоторой переменной и использовать это значение вне тела функции.

outside_result = pow_func(3)
print(outside_result)
# 9

# функцию, которая проверяет, является ли данная строка палиндромом или нет, и возвращает результат проверки.

print('My Bad Var')
# def check_palindrome(tx):
#    tx = str(list(input())
#             for n in tx:
#                print(n, )

print('Skill Var')


def check_palindrome(str_):
    str_ = str_.lower()    # Переводим в нижний регистр.
    str_ = str_.replace(" ", "")  # заменяем пробелы на ничто.

    if str_ == str_[::-1]:
        return True    # Если строка равна строке с конца до начала с обратным шагом.
    else:
        return False


check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True

# не могли сразу распечатать переменную inside_result вне тела функции


print('Skill BAD Var')


# def pow_func(base, n=2):
#    inside_result = base ** n
#    return inside_result
#
# print(inside_result)
# # ----> 5 print(inside_result)
# #       6 # 9


print('My GOOD Var')


def pow_func(base, n=2):
    inside_result = base ** n
    return inside_result


c = pow_func(6, 9)
print(c)
# ----> 5 print(inside_result)
#       6 # 9


print('My GOOD Var')


def check_palindrome(str_):
    str_ = str_.lower()  # Переводим в нижний регистр.
    str_ = str_.replace(" ", "")  # Заменяем пробелы на ничто.

    if str_ == str_[::-1]:
        return True  # Если строка равна строке с конца до начала с обратным шагом.
    else:
        return False


print(check_palindrome("test"))  # False
print(check_palindrome("А роза упала на лапу Азора"))  # True
print(check_palindrome("А пороо Влдлд"))