from pytest_bdd import scenario, given, when, then
from item_open import *

@scenario('../features/success.feature', 'Success message with order no')
def test_purchase():
    pass
