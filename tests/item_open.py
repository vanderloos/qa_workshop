from pytest_bdd import given, when, parsers
from selene.api import *

@given(parsers.parse('there is item: {item_url}'))
def item(item_url):
    config.browser_name = 'chrome'
    browser.open_url(item_url)

@given(parsers.parse('{button_text} button is available'))    
def check_button_available(button_text):
    ss('[title="Add to Cart"]')[1].text == button_text
    
    
@when(parsers.parse('I put {q} of it to cart'))
def set_qty(q):
    ss('#qty')[0].clear()
    ss('#qty')[0].send_keys(q)
    ss('[title="Add to Cart"]')[1].click()