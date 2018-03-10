from time import sleep

import pytest

from pages.search_results import SearchResults
from pages.start_screen import *


class TestSearch:
    @pytest.mark.search
    @pytest.mark.button
    def test_search_button_available(self):
        '''
        test that the saerch button is available
        '''
        assert StartScreen().search_button.should(be.clickable)

    @pytest.mark.search
    @pytest.mark.input
    def test_search_input_available(self):
        '''
        test that the saerch input available
        '''
        assert StartScreen().search_input.should(be.visible)
        
    
    @pytest.mark.debug
    def test_search_for_keyword(self):
        '''
        search for keyword "Testing"
        '''
        StartScreen().search_input.\
        send_keys('testing')
        StartScreen().search_button.click()
        
        assert SearchResults().num_of_posts == 20



