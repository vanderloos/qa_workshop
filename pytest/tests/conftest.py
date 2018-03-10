from time import sleep

import pytest
from selene.api import *
from os import environ
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


from pages.start_screen import *


@pytest.fixture(autouse=True, scope='session')
def browser_selene(request, base_url):
    cmd_option = request.config.getoption('driver').lower()
    if cmd_option == 'firefox':
        environ['MOZ_HEADLESS'] = '1'
        config.desired_capabilities = DesiredCapabilities.FIREFOX.copy()
        config.desired_capabilities["moz:firefoxOptions"] = {
            "prefs": {
                "security.sandbox.content.level": 4,
            }
        }

        config.browser_name = 'marionette'
    elif cmd_option == 'safari':
        config.browser_name = 'safari'
    else:
        config.browser_name = 'chrome'
    browser.open_url(base_url)
    yield






