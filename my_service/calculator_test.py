import pytest

from my_service.calculator import Calculator

@pytest.fixture
def sample_data():
    return {'a': 1, 'b': 2, 'sum': 3,'diff' : -1}

@pytest.fixture
def calc():
    return Calculator('simplee calculator')


def test_add(calc,sample_data):
    print(f'The calculator name is {calc.name}')
    assert calc.add(sample_data['a'], sample_data['b']) == sample_data['sum']

def test_minus(calc, sample_data):
    assert calc.minus(sample_data['a'], sample_data['b']) == sample_data['diff']

@pytest.mark.parametrize("num1,num2,expected",[(1,2,3),(2,3,5),(3,5,8),(3,4,6)])
def test_add_1(calc,num1,num2,expected):
    assert calc.add(num1,num2) == expected

def test_devide(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(num1=10,num2=0)