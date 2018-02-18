# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#chrome = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
#firefox = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) 

def test_lazytester_title(selenium):
    selenium.get('http://lazytesterua.blogspot.com/')
    print(selenium.title)
    assert selenium.title == u'Ледачий тестер'

