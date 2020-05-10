import time

from base_page import BasePage
from locators import PropertiesLocators

class Properties(BasePage):
    """
        Properties in rent/sell section
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.scroll_to_element(PropertiesLocators.PROPERTIES_SECTION)
    
    def assert_section_state(self):
        self.assert_element_text_contains(PropertiesLocators.PROPERTIES_TITLE, "inmuebles")
        assert self.count_elements(PropertiesLocators.PROPERTIES_SUBSECTIONS) == 4
        self._assert_subsection(1, "Apartamentos")
        self._assert_subsection(2, "Casas")
        self._assert_subsection(3, "Proyectos")

    def _assert_subsection(self, subsection_number, subsection_key):
        links = PropertiesLocators.SUBSECTION_LINKS
        links = (links[0], links[1] % subsection_number)
        title = PropertiesLocators.SUBSECTION_TITLES
        title = (title[0], title[1] % subsection_number)
        self.assert_element_text_contains(title, subsection_key)
        self.assert_element_text_contains(links, subsection_key)
