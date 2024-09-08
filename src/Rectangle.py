

class NonNegative:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("не может быть <figure> со стороной меньше 0!!!!")
        instance.__dict__[self.name] = value

class Rectangle:
    side_a = NonNegative()
    side_b = NonNegative()

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b * 2



