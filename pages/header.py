import allure
import time

from base_page import BasePage
from locators import HeaderLocators

class Header(BasePage):
    """
        Header navbar of the page
    """
    @allure.step
    def check_navbar_elements_visibility(self):
        time.sleep(5)
        self.assert_element_visible(HeaderLocators.NAVBAR_LOGO)
        self.assert_element_visible(HeaderLocators.NAVBAR_SEARCH)
        self.assert_element_visible(HeaderLocators.NAVBAR_NEWS)
        self.assert_element_visible(HeaderLocators.NAVBAR_TOOLS)
        self.assert_element_visible(HeaderLocators.NAVBAR_LOGIN)
        self.assert_element_visible(HeaderLocators.NAVBAR_PUBLISH)
    
    @allure.step
    def assert_m2_logo(self):
        self.click(HeaderLocators.NAVBAR_LOGO)
        time.sleep(5)
        self.assert_current_url("https://www.metrocuadrado.com/")

    @allure.step    
    def assert_search_property_form_visibility(self):
        self.click(HeaderLocators.NAVBAR_SEARCH)
        self.assert_element_visible(HeaderLocators.SEARCH_CONTRACT)
        self.assert_element_visible(HeaderLocators.SEARCH_TYPE)
        self.assert_element_visible(HeaderLocators.SEARCH_LOCATION_INPUT)
        self.assert_element_visible(HeaderLocators.SEARCH_BUTTON)
        self.assert_element_visible(HeaderLocators.SEARCH_LINK)
    
    @allure.step
    def assert_news_submenu_visibility(self):
        self.hover_to(HeaderLocators.NAVBAR_NEWS)
        assert self.count_elements(HeaderLocators.NEWS_SUBSECTIONS) == 2
        assert self.count_elements(HeaderLocators.NEWS_TREND_LINKS) == 6
        assert self.count_elements(HeaderLocators.NEWS_ARTICLES) == 3
        self.assert_element_visible(HeaderLocators.NEWS_MORE_BUTTON)

    @allure.step
    def assert_tools_submenu_visibility(self):
        self.hover_to(HeaderLocators.NAVBAR_TOOLS)
        assert self.count_elements(HeaderLocators.TOOLS_SUBSECTIONS) == 4
        assert self.count_elements(HeaderLocators.TOOLS_CALULATOR_LINKS) == 3
        assert self.count_elements(HeaderLocators.TOOLS_PROPERTY_LINKS) == 2
        assert self.count_elements(HeaderLocators.TOOLS_GUIDE_LINKS) == 5
        assert self.count_elements(HeaderLocators.TOOLS_GUIDE_ARTICLES) == 3
        self.assert_element_visible(HeaderLocators.TOOLS_MORE_BUTTON)

    @allure.step
    def assert_login_button(self):
        self.click(HeaderLocators.NAVBAR_LOGIN)
        time.sleep(5)
        self.assert_element_visible(HeaderLocators.LOGIN_FORM)

    @allure.step
    def assert_publish_button(self):
        self.click(HeaderLocators.NAVBAR_PUBLISH)
        time.sleep(5)
        self.assert_current_url("https://www.metrocuadrado.com/publicar-inmuebles/")