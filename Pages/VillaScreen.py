from Pages.BasePage import BasePage




class VillaScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_villa(self, city):
        self.click("villa_search_xpath")
        self.type("search_box_id", city)
        self.click_index("search_result_id", 0)
        self.click("calender_start_date_xpath")
        self.click("calender_end_date_xpath")
        self.click("continue_button_xpath")
        self.click("view_stays_xpath")

