import json
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


class UtilsDriver:
    _steam_driver = None
    _app_driver = None
    __quit_driver = True

    @classmethod
    def set_quit_driver(cls, mark):
        cls.__quit_mis_driver = mark

    @classmethod
    def get_steam_driver(cls):
        if cls._steam_driver is None:
            cls._steam_driver = webdriver.Chrome()
            cls._steam_driver.maximize_window()
            cls._steam_driver.get("https://store.steampowered.com")
        return cls._steam_driver

    @classmethod
    def quit_steam_driver(cls):
        if cls._steam_driver is not None and cls.__quit_driver:
            cls.get_steam_driver().quit()
            cls._steam_drive = None

    @classmethod
    def quit_app_driver(cls):
        if cls._app_driver is not None:
            cls.get_app_driver().quit()
            cls._app_driver = None


def get_element(location):
    wait = WebDriverWait(UtilsDriver.get_steam_driver(), 10, 0.5)
    element = wait.until(lambda x: x.find_element(*location))
    return element


def input_text(location, text):
    wait = WebDriverWait(UtilsDriver.get_steam_driver(), 10, 1)
    element = wait.until(lambda x: x.find_element(*location))
    element.clear() 
    element.send_keys(text)


def choice_channel(driver, element, channel):
    element.click()
    time.sleep(1)
    xpath = "//*[text()='{}']".format(channel)
    driver.find_element(By.XPATH, xpath).click()

def is_exist(driver, text):
    xpath = "//*[contains(text(), '{}')]".format(text)
    try:
        time.sleep(2)
        return driver.find_element(By.XPATH, xpath)
    except Exception as e:
        return False


def get_case_data(filename):
    with open(filename) as f:
        case = json.load(f)

    list_case_data = []
    for case_data in case.values():
        for item in case_data:
            data = []
            for key, value in item.items():
                data.append(value)
            list_case_data.append(tuple(data))
    return list_case_data

