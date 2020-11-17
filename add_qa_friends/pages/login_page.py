from add_qa_friends.parameters import USER_NAME, USER_PASSWORD
from selenium.webdriver.common.by import By


class LoginPage:

    __USERNAME = (By.XPATH, "//input[@id='username']")
    __PASSWORD = (By.XPATH, "//input[@id='password']")
    __SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element(*self.__USERNAME).send_keys(USER_NAME)
        self.driver.find_element(*self.__PASSWORD).send_keys(USER_PASSWORD)
        self.driver.find_element(*self.__SUBMIT_BUTTON).click()
