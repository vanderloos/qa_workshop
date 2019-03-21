import pytest
from random import randint
# from pytest_fixtures.slides.s00_simple_fixture.file_fixture import my_ints_file


@pytest.fixture(autouse=False, scope='class')
def prepare_my_ints_file():
    print('Conduct my preparations.')
    with open(r'data//text_file.txt', 'a') as file:
        for i in range(6):
            new_line = f'Line {randint(34, 42)}\n'
            file.writelines(new_line)
    print('End of preparations.')

    yield

    file = open(r'data//text_file.txt', 'w')
    file.writelines('')
    file.close()


# @pytest.fixture(autouse=True, scope='class')
# def prepare_my_ints_file(my_ints_file):
# """
# Using a fixture function from another file.
# """
#     file = my_ints_file
#     print('Conduct my preparations.')
#     for i in range(6):
#         new_line = f'Line {randint(34, 42)}\n'
#         file.writelines(new_line)
#     file.close()
#     print('End of preparations.')
#     yield
#     print('A kind of teardown.')
