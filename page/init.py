# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 17:11
# @Author  : Mr.Li

import unittest
from selenium import webdriver

class Init(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://test.admin.uzh.cn/site/login')
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()