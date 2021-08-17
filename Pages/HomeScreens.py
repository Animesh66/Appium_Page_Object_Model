from Pages.BasePage import BasePage
from Pages.HotelScreen import HotelScreen


class HomeScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_hotels(self):
        self.click("hotels_xpath")
        return HotelScreen(self.driver)  # return the object of the next screen/page

    def go_to_villas(self):
        self.click("villa_xpath")

    def got_to_trains(self):
        pass
