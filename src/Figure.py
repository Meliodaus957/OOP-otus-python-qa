from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(
                "аргумент figure должнен быть объектом класса Rectangle!!!!",
            )
        return self.area + figure.area


class NonNegative:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("не может быть фигуры со стороной меньше 0!!!!")
        instance.__dict__[self.name] = value
