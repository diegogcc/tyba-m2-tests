import pytest 
from selenium import webdriver
import sys      # add /pages to the sys.path

sys.path.insert(1, "../pages/")


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('headless')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver 
    driver.close()