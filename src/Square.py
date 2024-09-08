from Rectangle import Rectangle


class Square(Rectangle):
    def __init__ (self, side_a):
        super().__init__(side_a, side_a)
        self.side_a = side_a


s = Square(-1)
print(s.get_area)
print(s.get_perimeter)