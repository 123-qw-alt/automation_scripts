import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import utils

class web_1:
    @classmethod
    def add_operation(cls, input_text, input_text_2):
        input_element = By.XPATH, '// *[ @ id = "store_nav_search_term"]'
        utils.input_text(input_element, input_text)
        time.sleep(1)
        choose_element = By.XPATH, "//*[@data-ds-itemkey='0_1097150']"
        utils.get_element(choose_element).click()
        time.sleep(3)
        add_element = By.XPATH, '//div[@class="btn_addtocart"]/a[@href="javascript:addToCart(369927);"]/span'
        utils.get_element(add_element).click()
        categories_element = By.XPATH, '//div[@id="genre_tab"]//span//a[@class="pulldown_desktop"]'
        categories_element = utils.get_element(categories_element)
        action = ActionChains(utils.UtilsDriver.get_steam_driver())
        action.move_to_element(categories_element)
        action.perform()
        time.sleep(1)
        type_element = By.XPATH, '//*[@href="https://store.steampowered.com/category/multiplayer_coop/?snr=1_8_4__12"]'
        utils.get_element(type_element).click()
        utils.input_text(input_element, input_text_2)
        time.sleep(1)
        choose_element = By.XPATH, '//*[@data-ds-itemkey="0_728880"]'
        utils.get_element(choose_element).click()
        add_element = By.XPATH, '//a[@class="btn_green_steamui btn_medium"]'
        utils.get_element(add_element).click()
        time.sleep(3)


    @classmethod
    def delete_operation(cls, input_text, input_text_2, name):
        cls.add_operation(input_text, input_text_2)
        if name == 'fall guys':
            remove_item_1 = By.XPATH, '//div[@data-ds-itemkey="App_1097150"]//a[@class="remove_link"]'
            utils.get_element(remove_item_1).click()
            time.sleep(3)
            utils.UtilsDriver.get_steam_driver().get_screenshot_as_file("./img/img02.png")
        if name == 'overcooked':
            remove_item_2 = By.XPATH, '//*[@data-ds-itemkey="App_728880"]//a[@class="remove_link"]'
            utils.get_element(remove_item_2).click()
            time.sleep(3)
            utils.UtilsDriver.get_steam_driver().get_screenshot_as_file("./img/img01.png")
        if name == 'all':
            remove_item_1 = By.XPATH, '//div[@data-ds-itemkey="App_1097150"]//a[@class="remove_link"]'
            utils.get_element(remove_item_1).click()
            remove_item_2 = By.XPATH, '//*[@data-ds-itemkey="App_728880"]//a[@class="remove_link"]'
            utils.get_element(remove_item_2).click()
            utils.UtilsDriver.get_steam_driver().get_screenshot_as_file("./img/img03.png")

    @classmethod
    def remove_all_items(cls):
        remove_all_element = By.XPATH, '//*[@class ="remove_ctn"]'
        utils.get_element(remove_all_element).click()
        agree_element = By.XPATH, '// *[@class ="btn_green_steamui btn_medium"]'
        utils.get_element(agree_element).click()

    @classmethod
    def check_item_number(cls, input_text, input_text_2,):
        cls.add_operation(input_text, input_text_2)
        item_number_element = By.XPATH, '//*[@id="cart_item_count_value"]'
        item_number = utils.get_element(item_number_element).text
        return item_number

    @classmethod
    def check_remove_item(cls, input_text, input_text_2, item):
        cls.delete_operation(input_text, input_text_2, item)
        total_amount_element = By.XPATH, '//*[@id="cart_estimated_total"]'
        total_amount = utils.get_element(total_amount_element).text
        if item != 'all':
            cls.remove_all_items()
        return total_amount





