from Rectangle import Rectangle
from abc import ABC

class Square(Rectangle):
    def __init__ (self, side_a):
        super().__init__(side_a, side_a)
        self.side_a = side_a


s = Square(5)
print(s.add_area(figure=s))