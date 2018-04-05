import pytest
from inheritance import Car
from random import randint
from time import sleep

class TestTesla:
    def test_tesla_popltn1(self):
        tesla = Car('Roadster', 2,3,[], 6)
        tesla.send_peeps_here(1)
        assert tesla.population == 1
    
    @pytest.mark.mark1
    @pytest.mark.mark2
    def test_tesla_popltn2(self):
        tesla = Car('Roadster', 2,3,[], 6)
        tesla.send_peeps_here(2)
        assert tesla.population == 2, 'Wrong population!!!111'
    
    @pytest.mark.mark1
    def test_tesla_popltn_dot5(self):
        tesla = Car('Roadster', 2,3,[], 6)
        tesla.send_peeps_here(.5)
        assert tesla.population == .5
    @pytest.mark.mark2
    def test_tesla_popltn_1000(self):
        tesla = Car('Roadster', 2,3,[], 6)
        tesla.send_peeps_here(1000)
        assert tesla.population == 2

        
@pytest.mark.parametrize('mass', [randint(0,1000000) for x in range(10)])
class TestsParametrizedHardly:
    names = ['Roadster', 'Model S', 'SpaceX']  
    @pytest.mark.parametrize(('name_expected'), names)
    def test_car_name_positive(self, name_expected, mass):
        #name_expected = 'Roadster'
        tesla = Car(name_expected, mass,3,[], 6)
        assert tesla.name == name_expected
        
    def test_car_name_whitespace_negative(self, mass):
        name_not_alnum = 'Tesls-Roadster'
        with pytest.raises(NameError):
            Car(name_not_alnum, mass,3,[], 6)
        