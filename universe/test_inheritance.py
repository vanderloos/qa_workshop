import pytest
from inheritance import Car


def test_tesla_popltn1():
    tesla = Car('Roadster', 2,3,6, [])
    tesla.send_peeps_here(1)
    assert tesla.population == 1

def test_tesla_popltn2():
    tesla = Car('Roadster', 2,3,6, [])
    tesla.send_peeps_here(2)
    assert tesla.population == 2, 'Wrong population!!!111'
    
def test_tesla_popltn_dot5():
    tesla = Car('Roadster', 2,3,6, [])
    tesla.send_peeps_here(.5)
    assert tesla.population == .5

def test_tesla_popltn_1000():
    tesla = Car('Roadster', 2,3,6, [])
    tesla.send_peeps_here(1000)
    assert tesla.population == 2
    

def test_car_name_positive():
    name_expected = 'Roadster'
    tesla = Car(name_expected, 2,3,6, [])
    assert tesla.name == name_expected
    
def test_car_name_whitespace_negative():
    name_not_alnum = 'Tesls Roadster'
    with pytest.raises(NameError):
        Car(name_not_alnum, 2,3,6, [])
    