import pytest
import requests

from my_service.calculator import Calculator


@pytest.fixture(scope="module")
def calculator_the_best():
    return Calculator()


def test_add(calculator_the_best):
    assert calculator_the_best.add(2, 3) == 5

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (1, 1, 2),
    (0, 0, 0)
])
def test_add_parametrized(calculator_the_best, a, b, expected):
    assert calculator_the_best.add(a, b) == expected

def test_api():
    response = requests.get("https://google.com")
    assert response.status_code == 200
    print(f'The status code is {response.status_code}')
 