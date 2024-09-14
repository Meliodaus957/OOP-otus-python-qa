from src.Triangle import Triangle


def test_int_area(negative_int_test_triangle):
    side_a, side_b, side_c, h, area = negative_int_test_triangle
    t = Triangle(side_a, side_b, side_c, h)
    assert t.area == area, 'Area not should be negative'


def test_triangle_area_positive(positive_test_area_triangle):
    side_a, side_b, side_c, h, area = positive_test_area_triangle
    t = Triangle(side_a, side_b, side_c, h)
    assert t.area == area, f'Area should be {area}'


def test_triangle_area_negative(negative_test_area_triangle):
    side_a, side_b, side_c, h, area = negative_test_area_triangle
    t = Triangle(side_a, side_b, side_c, h)
    assert t.area == area, f'Area not should be {area}'


def test_triangle_perimeter_positive(positive_test_perimeter_triangle):
    side_a, side_b, side_c, h, perimeter = positive_test_perimeter_triangle
    t = Triangle(side_a, side_b, side_c, h)
    assert t.perimeter == perimeter, f'Area should be {perimeter}'


def test_triangle_perimeter_negative(negative_test_perimeter_triangle):
    side_a, side_b, side_c, h, perimeter = negative_test_perimeter_triangle
    t = Triangle(side_a, side_b, side_c, h)
    assert t.perimeter == perimeter, f'Area should be {perimeter}'
