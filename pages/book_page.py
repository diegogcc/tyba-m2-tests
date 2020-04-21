from base_page import BasePage
from locators import BookPageLocators

class BookPage(BasePage):
    """
    These tests are base on the asumption that the first result of the search
    will always be the Wikipedia article.
    """
    def __init__(self, driver):
        super().__init__(driver)

    def assert_article_title(self, expected):
        self.assert_element_text_contains(BookPageLocators.ARTICLE_TITLE, expected)