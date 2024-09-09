import math
from src.Figure import NonNegative
from Figure import Figure


class Circle(Figure):

    r = NonNegative

    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return math.pi * self.r ** 2

    @property
    def perimeter(self):
        return 2 * (math.pi * self.r)


c = Circle(5)

print(c.area)
print(c.perimeter)
