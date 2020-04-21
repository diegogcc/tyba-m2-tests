from selenium.webdriver.common.by import By

class CommonLocators:
    SEARCH_BAR = (By.NAME, "q")
    CLEAR_BUTTON = (By.CSS_SELECTOR, ".clear-button")
    FIRST_SUGGESTION = (By.CSS_SELECTOR, "[role='listbox'] > li:nth-child(1)")

class HomePageLocators:
    SEARCHBAR_GOOGLE_BUTTON = (By.CSS_SELECTOR, "center:nth-child(2) > input:nth-child(1)")
    SEARCHBAR_LUCKY_BUTTON = (By.CSS_SELECTOR, "center:nth-child(2) > input:nth-child(2)")
    LANGUAGE_BUTTON = (By.CSS_SELECTOR, "#SIvCob > a")

class ResultsPageLocators:
    FIRST_RESULT_LINK = (By.CSS_SELECTOR, "#rso > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)")
    SUGGESTED_QUERY_LINK = (By.CSS_SELECTOR, "#taw > div > div > p > a")

class BookPageLocators:
    ARTICLE_TITLE = (By.CSS_SELECTOR, "#firstHeading.firstHeading > i")
