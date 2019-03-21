import pytest


@pytest.fixture()
def my_fixture():
    return 'we are around here...'


def test_my_overrrrriden(my_fixture):
    assert 'oh my test!' == my_fixture
