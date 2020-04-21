from base_page import BasePage
from locators import ResultsPageLocators

class ResultsPage(BasePage):
    """
    Once the user searches for a query, they'll go to the results page, 
    which shows a list of possible matches (results).
    """
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_result(self):
        self.click(ResultsPageLocators.FIRST_RESULT_LINK)

    def assert_suggested_query(self, expected):
        self.assert_element_text_contains(ResultsPageLocators.SUGGESTED_QUERY_LINK, expected)

    def follow_suggested_query(self):
        self.click(ResultsPageLocators.SUGGESTED_QUERY_LINK)