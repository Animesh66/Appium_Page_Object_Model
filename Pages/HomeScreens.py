from Pages.BasePage import BasePage


class HomeScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_hotels(self):
        self.click("hotels_xpath")

    def go_to_villas(self):
        self.click("villa_xpath")

    def got_to_trains(self):
        pass
