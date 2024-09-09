import math
from src.Figure import NonNegative
from Figure import Figure

class Circle(Figure):

    r = NonNegative

    def __init__(self, r):
        self.r = r

    @property
    def get_area(self):
        return math.pi * self.r ** 2

    @property
    def get_perimeter(self):
        return 2 * (math.pi * self.r)


c = Circle(5)

print(c.get_area)
print(c.get_perimeter)
