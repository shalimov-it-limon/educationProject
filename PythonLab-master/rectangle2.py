class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

# Добавлю еще один класс.


class Square:   # Square (квадрат), который принимает в качестве аргумента одну сторону.
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2     # Возведение одной стороны в квадрат