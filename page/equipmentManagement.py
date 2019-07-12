# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 14:23
# @Author  : Mr.Li

from page.login import *
import time

class equipmentManagement(login):
    deviceManagement_loc = (By.XPATH, '//*[@id="w1"]/li[3]/a')
    deviceManagement2_loc = (By.ID, 'w4')
    getDeviceManagement_loc = (By.CLASS_NAME, 'panel-title')

    def enterEquipmentManagement(self):      # 进入删除列表页面
        self.Logins()
        self.findElement(*self.deviceManagement_loc).click()
        time.sleep(1)
        gf = self.findElement(*self.deviceManagement2_loc)
        nhg = gf.find_elements_by_tag_name('li')
        for gdf in nhg:
            if gdf.text == '设备管理':
                gdf.click()
                time.sleep(2)
                break
        A = self.findElement(*self.getDeviceManagement_loc).text
        return A
