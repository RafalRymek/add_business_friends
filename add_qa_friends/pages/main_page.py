from add_qa_friends.parameters import SEARCH_INPUT
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class MainPage:

    timeout = 5

    __SEARCH_INPUT = (By.XPATH, "//input[@class ='search-global-typeahead__input always-show-placeholder']")
    __FIND_USERS_BUTTON = (By.XPATH, "//button[@aria-label='Zobacz wyniki tylko dla Osoby']")

    def __init__(self, driver):
        self.driver = driver

    def find_friends(self, ):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(self.__SEARCH_INPUT))
            element.send_keys(SEARCH_INPUT)
            element.send_keys(Keys.ENTER)
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(self.__FIND_USERS_BUTTON)
            ).click()
        except (NoSuchElementException, TimeoutException):
            pass
