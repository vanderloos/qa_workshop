from pages.types import *


class SearchResults(Page):
    @property
    def num_of_posts(self):
        return len(browser.elements(by.xpath('//*[@itemprop="blogPost"]')))
