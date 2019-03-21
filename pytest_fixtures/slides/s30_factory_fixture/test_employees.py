import pytest


@pytest.mark.parametrize('position', ('Senior Automation QA', 'Jun'))
#@pytest.mark.parametrize('artificial_name', ('Mike', 'Gregory', 'Vasyl'))
def test_create_employee_status(make_employee, artificial_name, position):
    assert make_employee(artificial_name, position).status_code == 201

