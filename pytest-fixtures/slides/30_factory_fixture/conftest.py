import json

import pytest
import requests


def pytest_addoption(parser):
    '''New command line parameter to pass the URL'''
    parser.addoption("--url", action="store", default="http://example.com")


@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def make_employee(url):
    raise Exception("OLOLOLOO!!!!")
    def _make_employee(name, position):
        data = {"name": name,
                "position": position
                }
        return requests.post(url,
                             headers={'content-type':
                                          'application/json'},
                             data=json.dumps(data))\

    return _make_employee


@pytest.fixture(params=['Robocop', 'Terminator'])
def artificial_name(request):
    return request.param
