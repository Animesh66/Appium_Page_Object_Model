from Pages.test_BasePage import TestBasePage


class TestHomeScreen(TestBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def test_go_to_hotels(self):
        self.click("hotels_xpath")

    def test_go_to_villas(self):
        self.click("villa_xpath")

    def test_got_to_trains(self):
        pass
