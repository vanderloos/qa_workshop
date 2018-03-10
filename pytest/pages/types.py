from selene.api import *
from selene.elements import SeleneElement


class Page:
    pass


class Panel(Page):
    pass


class UIElement(SeleneElement):
    def __new__(cls, locator):
        SeleneElement.click_ = cls.click_
        return s(locator)

    def click_(self):
        self.click()
        return browser


class Button(UIElement):
    pass


