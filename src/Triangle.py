from src.Figure import Figure
from src.Figure import NonNegative


class Triangle(Figure):

    a = NonNegative()
    b = NonNegative()
    c = NonNegative()
    h = NonNegative()

    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    @property
    def area(self):
        return self.a + self.b + self.c

    @property
    def perimeter(self):
        return 1/2 * self.a * self.h


t = Triangle(5, 10, 12, 7)
print(t.area)
print(t.perimeter)
