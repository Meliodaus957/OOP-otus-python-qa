import pytest


@pytest.fixture
def negative_int_test():
    print("\n Start API")
    print("\n Start DB")

    yield -3, 5, 16

    print("\n End API")
    print('\n End DB')


@pytest.fixture
def negative_int_test_circle():
    print("\n Start API")
    print("\n Start DB")

    yield -3, 15

    print("\n End API")
    print('\n End DB')


@pytest.fixture
def negative_int_test_triangle():
    print("\n Start API")
    print("\n Start DB")

    yield -3, 5, 16, 3, 30

    print("\n End API")
    print('\n End DB')


@pytest.fixture
def negative_test_area_rectangle_square():
    print("\n Start API")
    print("\n Start DB")

    yield 3, 5, 16

    print("\n End API")
    print('\n End DB')


@pytest.fixture
def positive_test_area_rectangle_square():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 5, 15

    print("\n End API")
    print('\n End DB')


@pytest.fixture
def positive_test_perimeter_rectangle_square():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 5, 16

    print("\n End API")
    print('\n End DB')


@pytest.fixture
def negative_test_perimeter_rectangle_square():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 5, 15

    print("\n End API")
    print('\n End DB')

@pytest.fixture
def positive_test_area_circle():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 28.274333882308138

    print("\n End API")
    print('\n End DB')


@pytest.fixture
def negative_test_area_circle():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 28

    print("\n End API")
    print('\n End DB')

@pytest.fixture
def positive_test_perimeter_circle():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 18.84955592153876

    print("\n End API")
    print('\n End DB')

@pytest.fixture
def negative_test_perimeter_circle():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 18

    print("\n End API")
    print('\n End DB')


@pytest.fixture
def positive_test_area_triangle():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 18, 4, 5, 25

    print("\n End API")
    print('\n End DB')

@pytest.fixture
def negative_test_area_triangle():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 18, 4, 5, 20

    print("\n End API")
    print('\n End DB')

@pytest.fixture
def positive_test_perimeter_triangle():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 18, 4, 5, 7.5

    print("\n End API")
    print('\n End DB')

@pytest.fixture
def negative_test_perimeter_triangle():
    print('\n Start API')
    print('\n Start DB')

    yield 3, 18, 4, 5, 8

    print("\n End API")
    print('\n End DB')