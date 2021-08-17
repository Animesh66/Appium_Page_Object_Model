from BaseTest import BaseTest
import pytest

from Utilities import dataProvider


class Test_SearchHotels(BaseTest):

    @pytest.fixture("city", dataProvider.get_data("LoginTest"))
    def test_search_hotels(self, city):
