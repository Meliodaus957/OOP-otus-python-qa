from src.Circle import Circle
import pytest

@pytest.mark.parametrize(
    "side_a, area",
    [
        (3, 28.26)
    ]
)
def test_positive_area_circle(side_a, area):
    c = Circle(side_a)
    assert c.area == area, f'Area should be {area}'


def test_negative_area_circle(negative_test_area_circle):
    side_a, area = negative_test_area_circle
    c = Circle(side_a)
    assert c.area == area, f'Area not should be {area}'


def test_positive_perimeter_circle(positive_test_perimeter_circle):
    side_a, perimeter = positive_test_perimeter_circle
    c = Circle(side_a)
    assert c.perimeter == perimeter, f'Perimeter should be {perimeter}'


def test_negative_perimeter_circle(negative_test_perimeter_circle):
    side_a, perimeter = negative_test_perimeter_circle
    c = Circle(side_a)
    assert c.area == perimeter, f'Perimeter not should be {perimeter}'


def test_negative_int_circle_area(negative_int_test_circle):
    side_a, perimeter = negative_int_test_circle
    c = Circle(side_a)
    assert c.area == perimeter, 'Perimeter not should be negative'
