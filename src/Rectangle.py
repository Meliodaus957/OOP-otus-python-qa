from src.Figure import Figure
from src.Figure import NonNegative


class Rectangle(Figure):

    side_a = NonNegative()
    side_b = NonNegative()

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2

r = Rectangle(3, 5)

print(r.area)
print(r.perimeter)

print(r.add_area(figure=r))