class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def resize_full_page(self, resolution: tuple) -> None:
        self.driver.set_window_size(*resolution)
        self.driver.set_window_size(
            resolution[0],
            self.driver.execute_script("return document.body.parentNode.scrollHeight", )
        )
