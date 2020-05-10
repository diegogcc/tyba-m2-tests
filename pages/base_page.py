from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

class BasePage:
    """
    BasePage class will hold common elements and functionalities
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.metrocuadrado.com/calculadora-credito-hipotecario-vivienda/")

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def read_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def read_element_value(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute("value")

    def assert_element_value_contains(self, by_locator, expected):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        print(element.get_attribute("value"))
        assert expected.lower() in str(element.get_attribute("value")).lower()
    
    def assert_element_text_contains(self, by_locator, expected):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert expected.lower() in str(element.text).lower()
    
    def assert_element_text_matches(self, by_locator, expected):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.text == expected

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
    
    def assert_current_url(self, expected):
        assert self.driver.current_url == expected
    
    def assert_element_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.is_enabled()

    def assert_element_not_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert not element.is_enabled()
    
    def assert_element_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        assert element.is_displayed()
    
    def assert_element_not_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        assert not element.is_displayed()
        
    def count_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return len(elements)
    
    def get_element_attribute(self, by_locator, attribute):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute)

    def enter_keys(self, by_locator, keys):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(keys)
    
    def select_dropdown_by_index(self, by_locator, index):
        element = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        element.select_by_index(index)
    
    def select_dropdown_by_text(self, by_locator, text):
        element = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        element.select_by_visible_text(text)
    
    def scroll_to_element(self, by_locator):
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        actions.move_to_element(element).perform()
