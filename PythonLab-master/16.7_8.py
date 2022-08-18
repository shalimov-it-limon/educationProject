# наследование из основного прямоугольника (Rectangle): возьмем оттуда все свойства,
# такие как width (ширина) и height (высота), и создадим псевдопрямоугольник r1.


class Rectangle:
    def __init__(self, wight, height):
        self.wight = wight
        self.height = height

    def getWight(self):
        return self.wight

    def  getHeight(self):
        return self.height

# Метод, рассчитывающий площадь.

def getArrea(self):
    return self.wight * self.height

# Прямоугольник r1 должен наследовать те же характеристики,
# что и базовый прямоугольник (Rectangle). Выполняется это через импортирование.

