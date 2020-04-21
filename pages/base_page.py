from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import CommonLocators

class BasePage:
    """
    BasePage class will hold common elements and functionalities
    """
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def read_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def assert_element_text_contains(self, by_locator, expected):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert expected.lower() in str(element.text).lower()
    
    def assert_element_text_matches(self, by_locator, expected):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.text == expected
    
    def enter_query(self, query):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CommonLocators.SEARCH_BAR)).send_keys(query)
    
    def clear_query(self):
        self.click(CommonLocators.CLEAR_BUTTON)
    
    def search_by_first_suggestion(self, query):
        self.enter_query(query)
        self.click(CommonLocators.FIRST_SUGGESTION)