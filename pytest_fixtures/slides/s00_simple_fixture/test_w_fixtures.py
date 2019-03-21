import pytest


@pytest.fixture()
def ints():
    ints = []
    with open(r'data//text_file.txt', 'r') as file:
        for line in file:
            try:
                num = int(line.split()[-1])
                ints.append(num)
            except (ValueError, IndexError):
                pass
    return ints


def test_42(ints):
    print(f'Test {ints}.')
    assert 42 in ints
