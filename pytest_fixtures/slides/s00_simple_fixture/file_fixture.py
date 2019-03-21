import pytest
from random import randint


@pytest.fixture(scope='session')
def my_ints_file():
    print('Opening the file.')
    file =open(r'data//text_file.txt', 'a')
    yield file
    with open(r'data//text_file.txt', 'w') as file:
        print('Clean up the file.....')
        file.writelines('')
        file.close()

