from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("/Users/animeshmukherjee/PycharmProjects/pythonProject/Appium_Page_Object_Model/Configurations/conf.ini")
    return config.get(section, key)
