import time
from BaseTest import BaseTest
import pytest
from Pages.HomeScreens import HomeScreen
from Utilities import dataProvider


class Test_SearchVillas(BaseTest):

    @pytest.mark.parametrize("city", dataProvider.get_data("LoginTest"))
    def test_search_villas(self, city):
        home_screen = HomeScreen(self.driver)
        home_screen.go_to_villas().search_villa(city)  # this is method chaining

