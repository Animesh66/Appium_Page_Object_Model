import logging
from Utilities.LogUtil import Logger
from Utilities import configReader

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_xpath"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).click()

        elif str(locator).endswith("_id"):
            self.driver.find_element_by_id(configReader.readConfig("locators", locator)).click()

        log.logger.info("Clicking on the element: " + str(locator))

    def click_index(self, locator, index):
        if str(locator).endswith("_xpath"):
            self.driver.find_elements_by_xpath(configReader.readConfig("locators", locator))[index].click()

        elif str(locator).endswith("_id"):
            self.driver.find_elements_by_id(configReader.readConfig("locators", locator))[index].click()

        log.logger.info("Clicking on the element: " + str(locator) + " with index " + str(index))

    def type(self, locator, value):
        if str(locator).endswith("_xpath"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).send_keys(value)

        elif str(locator).endswith("_id"):
            self.driver.find_element_by_id(configReader.readConfig("locators", locator)).send_keys(value)

        log.logger.info("Typing on the element: " + str(locator) + " entered the value as: " + str(value))

    def get_text(self, locator):
        if str(locator).endswith("_xpath"):
            text = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).text

        elif str(locator).endswith("_id"):
            text = self.driver.find_element_by_id(configReader.readConfig("locators", locator)).text

        log.logger.info("Getting text from an element: " + str(locator))
        return text