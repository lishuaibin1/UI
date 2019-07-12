# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 20:24
# @Author  : Mr.Li

import time
from page.login import *
from page.init import Init


class Login(Init, login):

    def test_login_null(self):
        '''验证用户名密码为空'''
        self.clickLogin()
        time.sleep(2)
        test = self.driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/p').text
        self.assertEqual(test, '用户名不能为空。')

    def test_login_success(self):
        '''验证登录成功'''
        self.Logins()
        title = self.driver.find_element_by_class_name('text-center').text
        self.assertEqual(title, '优装汇')
