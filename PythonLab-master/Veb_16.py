# Вычеслить периметр и площадь треугольника по 3 сторонам.
# Вычеслить периметр и площадь прямоугольника по высоте и ширине.
# Вычеслить площадь круга по радиусу.
import math
print('My GOOD VAR')


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter_triangle(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b):
            return self.a + self.b + self.c
        else:
            return 'Этот треугольник вырожденный.'

    def get_area_triangle(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b):
            p = (self.a + self.b + self.c) / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
            # return pow(p * (p - self.a) * (p - self.b) * (p - self.c), 1/2)
        else:
            return 'Этот треугольник вырожденный.'


triangle_1 = Triangle(6, 8, 5)
print(f'Периметр треугольника равен {triangle_1.get_perimeter_triangle()}')
print(f'Площадь треугольника равна {triangle_1.get_area_triangle()}')
# можно воспользоваться стандартной функцией возведения числа в степень.
# Дело в том, что квадратный корень - это возведение в степень 1/2.
# Синтаксис функции такой: pow(x, y)
# где x - число, возводимое в степень, а y - сама степень.


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_perimeter_rectangle(self):
        return (self.height + self.width) * 2

    def get_area_rectangle(self):
        return self.height * self.width


rectangle_1 = Rectangle(9, 19)
print(f'Периметр прямоугольника равен {rectangle_1.get_perimeter_rectangle()}')
print(f'Площадь прямоугольника равна {rectangle_1.get_area_rectangle()}')


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        p = 3.14
        return p * (self.r ** 2)


circle_1 = Circle(5)
print(f'Площадь круга равна {circle_1.get_area_circle()}')

# Сумма и произведение цифр введенного трехзначного числа.
num = input('Введите трехзначное число: ')
# class ThreeDigitNumber:

a = num % 100 == 0
b = num % 10 == 0
c = num % 1

