import logging
from Utilities.LogUtil import Logger
from Utilities import configReader

log = Logger(__name__, logging.INFO)


class test_BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith('xpath'):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).click()

        elif str(locator).endswith('id'):
            self.driver.find_element_by_id(configReader.readConfig("locators", locator)).click()

        log.logger.info("Clicking on element: ", str(locator))