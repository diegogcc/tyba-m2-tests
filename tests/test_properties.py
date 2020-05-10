import pytest 
import sys      # add /pages to the sys.path

sys.path.insert(1, "../pages/")

from properties import Properties

def test_properties_section_on_load(driver):
    """Load the page and see the state of the properties section.
    It should have 4 sections with link by locations"""
    properties = Properties(driver)
    properties.assert_section_state()