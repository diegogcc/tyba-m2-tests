'''
On the /tests folder run:
    '$ python3 -m unittest -v'
'''
import unittest
from selenium import webdriver
import sys 
# Add the pages to the sys.path

sys.path.insert(1, "../pages/")
import locators
from home_page import HomePage
from results_page import ResultsPage
from book_page import BookPage


class TestHomePageSearch(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--lang=en')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.home = HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    # def test_search_query_enter_first_result_and_verify_title(self):
    #     QUERY = 'the name of the wind'

    #     self.home.search_with_google_button_from_suggestion_list(QUERY)
        
    #     results = ResultsPage(self.driver)
    #     results.enter_first_result()

    #     article = BookPage(self.driver)
    #     article.assert_article_title(QUERY)

    # def test_search_query_with_suggestions_enter_first_result_and_verify_title(self):
    #     QUERY = 'the name of the wind'

    #     self.home.search_by_first_suggestion(QUERY)

    #     results = ResultsPage(self.driver)
    #     results.enter_first_result()

    #     article = BookPage(self.driver)
    #     article.assert_article_title(QUERY)

    # def test_search_query_with_typo_enter_first_result(self):
    #     WRONG_QUERY = 'the nam of the wind'
    #     RIGHT_QUERY = 'the name of the wind'

    #     self.home.search_with_google_button_from_suggestion_list(WRONG_QUERY)
        
    #     results = ResultsPage(self.driver)
    #     results.assert_suggested_query(RIGHT_QUERY)
    #     results.enter_first_result()

    #     article = BookPage(self.driver)
    #     article.assert_article_title(RIGHT_QUERY)

    # def test_search_query_with_typo_follow_suggestion_enter_first_result(self):
    #     WRONG_QUERY = 'the nam of the wind'
    #     RIGHT_QUERY = 'the name of the wind'

    #     self.home.search_with_google_button_from_suggestion_list(WRONG_QUERY)
        
    #     results = ResultsPage(self.driver)
    #     results.assert_suggested_query(RIGHT_QUERY)
    #     results.follow_suggested_query()
    #     results.enter_first_result()

    #     article = BookPage(self.driver)
    #     article.assert_article_title(RIGHT_QUERY)

    # def test_im_feeling_lucky_button(self):
    #     QUERY = 'the name of the wind'

    #     self.home.search_with_feeling_lucky_button_from_suggestion_list(QUERY)

    #     article = BookPage(self.driver)
    #     article.assert_article_title(QUERY)

    # def test_clear_query(self):
    #     QUERY = 'the name of the wind'

    #     self.home.enter_query(QUERY)
    #     self.home.clear_query_and_assert()


if __name__ == "__main__":
    unittest.main()