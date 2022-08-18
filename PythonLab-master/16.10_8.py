try:
    raise ZeroDivisionError # возбуждаем исключение ZeroDivisionError
except ArithmeticError: # ловим его родителя
    print("Hello from arithmetic error")


class MyException(Exception):  # создаём пустой класс – исключения
    pass

try:
    raise MyException("message")  # поднимаем наше исключение
except MyException as e:  # ловим его за хвост как шкодливого котёнка
    print(e)  # выводим информацию об исключении


class ParentException(Exception):  # создаём пустой класс – исключения потомка, наследуемся от exception
    pass


class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    pass


try:
    raise ChildException("message")  # поднимаем исключение-наследник
except ParentException as e:  # ловим его родителя
    print(e)  # выводим информацию об исключении

#  добавить собственные аргументы в конструктор,
#  дополнительно произвести какие либо операции, то можете


class ParentException(Exception):
    def __init__(self, message,
                 error):  # допишем к нашему пустому классу конструктор, который будет печатать дополнительно в консоль информацию об ошибке.
        super().__init__(message)  # помним про вызов конструктора родительского класса
        print(f"Errors: {error}")  # печатаем ошибку


class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    def __init__(self, message, error):
        super().__init__(message, error)


try:
    raise ChildException("message", "error")  # поднимаем исключение-наследник, передаём дополнительный аргумент
except ParentException as e:
    print(e)  # выводим информацию об исключении



# try:
#     text = input('Введите что-нибудь --> ')
# except EOFError:
#     print('Ну зачем вы сделали мне EOF?')
# except KeyboardInterrupt:
#     print('Вы отменили операцию.')
# else:
#     print('Вы ввели {0}'.format(text))

# Создать класс SquareException.
# Добавить в конструктор класса Square собственное исключение NonPositiveDigitException,
# унаследованное от ValueError,
# которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.


class SquareException(ValueError):
    pass


class NonPositiveDigitException(SquareException):
    pass


class Square:
    def __init__(self, a):
        self.a = a
        if a <= 0:
            raise NonPositiveDigitException('Сторона "а" задана неверно.')
        else:
            ...

    def get_area_square(self):
        return self.a ** 2     # Возведение одной стороны в квадрат


sq_1 = Square(5)
print(sq_1.get_area_square())
sq_2 = Square(-6)
print(sq_2.get_area_square())


# class NonPositiveDigitException(ValueError):
#     pass


# class Square:
#     def __init__(self, a):
#         self.a = a
#         if a <= 0:
#             raise NonPositiveDigitException('Неправильно указанна сторона квадрата')
#
#     def get_area_square(self):
#         return self.a ** 2
#
#
# sq_1 = Square(5)
# print(sq_1.get_area_square())
# sq_2 = Square(-6)
# print(sq_2.get_area_square())