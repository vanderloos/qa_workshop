from random import randint

import pytest


def test_42_int():
    ints = []
    with open(r'data//text_file.json', 'r') as file:
        for line in file:
            ints.append(int(line.split()[1]))
    assert 42 in ints


class Test34:
    @pytest.mark.usefixtures('my_steps', 'my_other_steps')
    def test_34_int(self):
        assert 34 == int('34')