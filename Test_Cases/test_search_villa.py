import time
from Test_Cases.BaseTest import BaseTest
import pytest
from Pages.HomeScreens import HomeScreen
from Utilities import dataProvider
from Utilities.scroll_util import ScrollUtil


class Test_SearchVillas(BaseTest):

    @pytest.mark.parametrize("city, villa", dataProvider.get_data("VillaTest"))
    def test_search_villas(self, city, villa):
        home_screen = HomeScreen(self.driver)
        home_screen.go_to_villas().search_villa(city)  # this is method chaining
        ScrollUtil.scrollToTextByAndroidUIAutomator(villa, self.driver)  # search for a particular villa
        time.sleep(3)
