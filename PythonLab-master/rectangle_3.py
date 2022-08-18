from rectangle2 import Rectangle

# Создаю 2 прямоугольника.

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# Выведу площади этих прмямоугольников.

print(rect_1.get_area())
print(rect_2.get_area())
print('-' * 20)

from rectangle2 import Rectangle, Square

# Создаю 2 прямоугольника.

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# Выведу площади этих прмямоугольников.

print(rect_1.get_area())
print(rect_2.get_area())

# Выведу квадрат одной стороны.
square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square())
print(square_2.get_area_square())
# ИЛИ
print(square_1.get_area_square(), square_2.get_area_square())
print('-' * 20)

# все объекты перенесу в единую коллекцию.

figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
    if isinstance(figure, Square):    # isinstance - проверка, принадлежит или нет.
                                      # Если фигура приндлежит классу Квадрат:
        print(figure.get_area_square())
    else:
        print(figure.get_area())

