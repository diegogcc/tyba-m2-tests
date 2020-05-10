import pytest 
import sys      # add /pages to the sys.path

sys.path.insert(1, "../pages/")

from header import Header

def test_header_elements_on_load(driver):
    """Load the page and verify that the correct elements are displayed
    on the navigation bar"""
    header = Header(driver)
    header.check_navbar_elements_visibility()

def test_click_m2_logo(driver):
    """Load the page and click on the metrocuadrado (m2) logo,
    the user should go to the Home Page"""
    header = Header(driver)
    header.assert_m2_logo()

def test_click_search_property_button(driver):
    """Load the page and click on the 'Bucar inmueble' button,
    the property search form should be displayed with the correct elements"""
    header = Header(driver)
    header.assert_search_property_form_visibility()

def test_hover_over_news_button(driver):
    """Load the page and hover over the 'Noticias y Tendencias' button, 
    the news and trends submenu should be displayed with the correct elements"""
    header = Header(driver)
    header.assert_news_submenu_visibility()

def test_hover_over_tools_button(driver):
    """Load the page and hover over the 'Herramientas' button,
    the tools submenu should be displayed with the correct elements"""
    header = Header(driver)
    header.assert_tools_submenu_visibility()

def test_login_button_user_not_logged(driver):
    """Load the page and click on the 'Ingresar' button when the user
    is not logged in yet.
    The user should be re-directed to the login form with the correct elements"""
    header = Header(driver)
    header.assert_login_button()

def test_click_publish_property_button(driver):
    """Load the page and click on the 'Publicar inmueble' button.
    The user should be re-directed to the publication page."""
    header = Header(driver)
    header.assert_publish_button()