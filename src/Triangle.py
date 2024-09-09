from Rectangle import Figure, NonNegative


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
    def get_area(self):
        return self.a + self.b + self.c

    @property
    def get_perimeter(self):
        return 1/2 * self.a * self.h


t = Triangle(0, 10, 12, 7)
print(t.get_area)
print(t.get_perimeter)
