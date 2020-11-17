from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class AddFriendPage:
    timeout = 5

    __ADD_FRIEND_BUTTON = (By.XPATH, "//button[@data-control-name='srp_profile_actions']")
    __SEND_INVITATION_BUTTON = (By.XPATH, "//button[@aria-label='Wyślij teraz']")
    __USER_CONTAINER = (By.XPATH, "//li[@class='search-result search-result__occluded-item ember-view']")
    __PROFILE = (By.XPATH, "//div[@data-test-search-result='PROFILE']")
    __SEARCH_RESULTS = (By.XPATH, "//ul[@class='search-results__list list-style-none ']")

    def __init__(self, driver):
        self.driver = driver

    def add_all_friends(self):
        add_button = self.driver.find_elements(*self.__ADD_FRIEND_BUTTON)
        for user in add_button:
            user.click()
            send_button = self.driver.find_elements(*self.__SEND_INVITATION_BUTTON)
            for invitation in send_button:
                invitation.click()
                user_row = self.driver.find_elements(*self.__PROFILE)
                for friend in user_row:
                    ActionChains(self.driver).move_to_element(friend).perform()
