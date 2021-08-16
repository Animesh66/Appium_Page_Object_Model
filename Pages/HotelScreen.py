from Pages.BasePage import BasePage


class HotelScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_hotels(self, city):
        self.click("search_button_xpath")
        self.click("search_anywhere_xpath")
        self.type("search_box_id", "Delhi")
        self.click_index("com.goibibo:id/lytLocationItem",0)
        self.click("search_button_xpath")

