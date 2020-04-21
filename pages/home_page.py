from base_page import BasePage
from locators import CommonLocators, HomePageLocators
import time

class HomePage(BasePage):
    """
    Home page of google.com
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.google.com/")
        self._change_google_lang_to_english()

    def search_with_google_button_from_suggestion_list(self, query):
        self.enter_query(query)
        self.click(HomePageLocators.SEARCHBAR_GOOGLE_BUTTON)

    def search_with_feeling_lucky_button_from_suggestion_list(self, query):
        self.enter_query(query)
        self.click(HomePageLocators.SEARCHBAR_LUCKY_BUTTON)

    def _change_google_lang_to_english(self):
        current_lang = self.read_element_text(HomePageLocators.LANGUAGE_BUTTON)
        if 'english' in str(current_lang).lower():
            self.click(HomePageLocators.LANGUAGE_BUTTON)
        else:
            print("Google is already in English")
    
    def clear_query_and_assert(self):
        self.click(CommonLocators.CLEAR_BUTTON)
        after_text = self.read_element_text(CommonLocators.SEARCH_BAR)
        assert not after_text