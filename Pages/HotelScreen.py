from Pages.BasePage import BasePage


class HotelScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_hotels(self, city):
        self.click("search_anywhere_xpath")
        self.type("search_box_id", city)
        self.click_index("search_result_id", 0)
        self.click("search_button_xpath")
