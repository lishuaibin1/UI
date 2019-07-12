# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 11:15
# @Author  : Mr.Li


from page.login import *
import time


class delete(login):
    deviceManagement_loc = (By.XPATH, '//*[@id="w1"]/li[3]/a')
    deviceManagement2_loc = (By.ID, 'w4')
    DeleteBounced_loc = (By.XPATH, '//*[@id="uzh-toolbar"]/div[2]/div/a[1]')
    saveDelete_loc = (By.XPATH, '//*[@id="ajaxCrudModal"]/div/div/div[3]/button')
    getDeleteList_loc = (By.CLASS_NAME, 'active')
    getEquipmentEmpty_loc = (By.CLASS_NAME, 'help-block')
    InputDeviceNumber_loc = (By.ID, 'deldriverform-driver_list')
    getInputDeviceNumber_loc = (By.CLASS_NAME, 'modal-title')
    deleteReason_loc = (By.ID, 'select2-deldriverform-reason_type-container')
    deleteReason2_loc = (By.ID, 'select2-deldriverform-reason_type-results')



    def enterDeleteList(self):      # 进入删除列表页面
        self.Logins()
        self.findElement(*self.deviceManagement_loc).click()
        time.sleep(1)
        gf = self.findElement(*self.deviceManagement2_loc)
        nhg = gf.find_elements_by_tag_name('li')
        for gdf in nhg:
            if gdf.text == '删除列表':
                gdf.click()
                time.sleep(2)
                break
        a = self.findElement(*self.getDeleteList_loc).text
        return a

    def DeleteBounced(self):        # 删除弹框
        self.findElement(*self.DeleteBounced_loc).click()

    def saveDelete(self):       # 确定删除
        self.findElement(*self.saveDelete_loc).click()

    def EquipmentEmpty(self):       # 输入设备为空
        self.DeleteBounced()
        time.sleep(1)
        self.saveDelete()
        time.sleep(1)
        b = self.findElement(*self.getEquipmentEmpty_loc).text
        return b

    def InputDeviceNumber(self):        # 设备号不在库
        self.DeleteBounced()
        time.sleep(1)
        self.findElement(*self.InputDeviceNumber_loc).send_keys('353445342700546331')
        time.sleep(1)
        self.saveDelete()
        time.sleep(2)
        c = self.findElement(*self.getInputDeviceNumber_loc).text
        return c

    def deleteReason(self):         # 删除原因选择
        self.DeleteBounced()
        time.sleep(1)
        self.findElement(*self.deleteReason_loc).click()
        time.sleep(1)
        d = self.findElement(*self.deleteReason2_loc)
        e = d.find_elements_by_tag_name('li')
        for f in e:
            if f.text == '回收报废':
                f.click()
                time.sleep(1)
                break
        g = self.findElement(*self.deleteReason_loc).get_attribute('title')
        return g








