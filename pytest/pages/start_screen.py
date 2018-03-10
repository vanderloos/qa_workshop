from pages.types import *


class StartScreen(Page):
    @property
    def search_button(self):
        return Button('input.gsc-search-button')

    @property    
    def search_input(self):
        return s('input.gsc-input')

