import time
from Test_Cases.BaseTest import BaseTest
import pytest
from Pages.HomeScreens import HomeScreen
from Utilities import dataProvider


class Test_SearchHotels(BaseTest):

    @pytest.mark.parametrize("city", dataProvider.get_data("LoginTest"))
    def test_search_hotels(self, city):
        home_screen = HomeScreen(self.driver)
        home_screen.go_to_hotels().search_hotels(city)  # this is method chaining

