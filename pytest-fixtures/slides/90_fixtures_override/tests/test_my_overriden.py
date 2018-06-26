import pytest

#
# @pytest.fixture()
# def my_fixture():
#     return 'we are near we are near we are nearwe are nearwe are nearwe are nearwe are near'


def test_my_overrrrriden(my_fixture):
    assert 'oh my test!' == my_fixture
