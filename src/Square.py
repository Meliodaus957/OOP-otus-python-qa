from Rectangle import Rectangle
from src.Figure import NonNegative
from Figure import Figure


class Square(Rectangle, Figure):

    side_a = NonNegative()

    def __init__(self, side_a):
        super().__init__(side_a, side_a)
        self.side_a = side_a


s = Square(5)
print(s.add_area(figure=s))
