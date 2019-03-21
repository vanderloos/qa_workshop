import pytest


@pytest.fixture()
def my_fixture():
    return "We're above the tests directory!"
