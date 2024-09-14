from src.Rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    "side_c, side_d, area_z",
    [
        (3, 5, 15),
        (3.5, 5.5, 19.25)
    ],
    ids=['integer', 'float']
)
def test_rectangle_area_positive(side_c, side_d, area_z):
    r = Rectangle(side_c, side_d)
    assert r.area == area_z, f'area should be {area_z}'


def test_rectangle_integer_negative(negative_test_area_rectangle_square):
    side_a, side_b, area = negative_test_area_rectangle_square
    r = Rectangle(side_a, side_b)
    assert r.area == area, 'Area not should be 15'


def test_rectangle_integer_positive(positive_test_area_rectangle_square):
    side_a, side_b, area = positive_test_area_rectangle_square
    r = Rectangle(side_a, side_b)
    assert r.area == area, 'Area should be 15'


def test_rectangle_perimeter_positive(positive_test_perimeter_rectangle_square):
    side_a, side_b, perimeter = positive_test_perimeter_rectangle_square
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, "Perimeter should be 16"


def test_rectangle_perimeter_negative(negative_test_perimeter_rectangle_square):
    side_a, side_b, perimeter = negative_test_perimeter_rectangle_square
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, "Perimeter not should be 16"


def test_int_area(negative_int_test):
    side_a, side_b, area = negative_int_test
    r = Rectangle(side_a, side_b)
    assert r.area == area, 'Area not should be negative'
