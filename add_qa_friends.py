import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from add_qa_friends.pages.login_page import LoginPage
from add_qa_friends.pages.main_page import MainPage
from add_qa_friends.pages.base_page import BasePage
from add_qa_friends.pages.add_friend_page import AddFriendPage
from add_qa_friends.parameters import BASE_URL, LOGIN_ENDPOINT, SCREEN_RESOLUTION


class AddQaFriends(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.add_friend_page = AddFriendPage(self.driver)
        self.driver.maximize_window()
        self.driver.get(f"{BASE_URL}{LOGIN_ENDPOINT}")

    def test_add_qa_friends(self):
        # self.base_page.resize_full_page(SCREEN_RESOLUTION)
        self.login_page.login()
        self.main_page.find_friends()
        self.add_friend_page.add_all_friends()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()