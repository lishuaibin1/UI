# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 21:08
# @Author  : Mr.Li


from selenium.webdriver.support.expected_conditions import NoAlertPresentException

class WEB:
    def __init__(self, driver):
        self.driver = driver

    def findElement(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except NoAlertPresentException as e:
            print(e.args[0])
