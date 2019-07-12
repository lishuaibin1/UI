# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 21:17
# @Author  : Mr.Li

from selenium.webdriver.common.by import By
from base.base import WEB

class login(WEB):
    clickLogin_loc = (By.NAME, 'login-button')
    username_loc = (By.ID, 'loginform-username')
    password_loc = (By.ID, 'loginform-password')


    def clickLogin(self):
        self.findElement(*self.clickLogin_loc).click()

    def inputUsername(self, username):
        self.findElement(*self.username_loc).send_keys(username)

    def inputPassword(self, password):
        self.findElement(*self.password_loc).send_keys(password)

    def Logins(self, username='李帅宾', password='111111'):
        self.inputUsername(username)
        self.inputPassword(password)
        self.clickLogin()
