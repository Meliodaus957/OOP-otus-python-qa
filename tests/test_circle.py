from src.Circle import Circle


def test_positive_area_circle(positive_test_area_circle):
    side_a, area = positive_test_area_circle
    c = Circle(side_a)
    assert c.area == area, 'Area should be 28.2743'


def test_negative_area_circle(negative_test_area_circle):
    side_a, area = negative_test_area_circle
    c = Circle(side_a)
    assert c.area == area, 'Area not should be 28'


def test_positive_perimeter_circle(positive_test_perimeter_circle):
    side_a, perimeter = positive_test_perimeter_circle
    c = Circle(side_a)
    assert c.perimeter == perimeter, 'Perimeter should be 18.84955592153876'


def test_negative_perimeter_circle(negative_test_perimeter_circle):
    side_a, perimeter = negative_test_perimeter_circle
    c = Circle(side_a)
    assert c.area == perimeter, 'Perimeter not should be 18'


def test_negative_int_circle_area(negative_int_test_circle):
    side_a, perimeter = negative_int_test_circle
    c = Circle(side_a)
    assert c.area == perimeter, 'Perimeter not should be negative'
