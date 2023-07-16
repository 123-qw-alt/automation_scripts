import time

import allure
import pytest

import utils
from config import BaseDir
from page import main_function
from utils import UtilsDriver, get_case_data

case_data = get_case_data(BaseDir+"/data/web/remove_item_data.json")

@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.run(order=1001)
class TestLogin:
    def setup_class(self):
        self.add_delete_function = main_function.web_1

    def teardown_class(self):
        UtilsDriver.get_steam_driver().current_window_handle
        UtilsDriver.quit_steam_driver()


    @pytest.fixture(autouse=True)
    def start_and_teardown(self):
        assert True
        yield
        utils.UtilsDriver.get_steam_driver().get("https://store.steampowered.com")



    @pytest.mark.parametrize("item, item_1, item_2, expect", case_data)
    def test_payment_amount(self, item, item_1, item_2, expect):
        total_amount = self.add_delete_function.check_remove_item(item_1, item_2, item)
        allure.attach(utils.UtilsDriver.get_steam_driver().get_screenshot_as_png(), "screen capture", allure.attachment_type.PNG)
        assert total_amount == expect

#add comment
#add comment


