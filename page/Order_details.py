# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 11:21
# @Author  : Mr.Li

from page.dingdan import *
import datetime


class Order(OrderManagement):
    submitOrders_loc = (By.XPATH, '//*[@id="w4"]/div[1]/div/div[2]/div/a[1]')
    confirm_loc = (By.XPATH, '//*[@id="ajaxCrudModal"]/div/div/div[3]/button[1]')
    Save_loc = (By.XPATH, '//*[@id="ajaxCrudModal"]/div/div/div[3]/button')
    getSubmitOrders_loc = (By.XPATH, '//*[@id="figure1"]/span')
    CancelOrder_loc = (By.XPATH, '//*[@id="w4"]/div[1]/div/div[2]/div/a[2]')
    SaveCancelOrder_loc = (By.XPATH, '//*[@id="ajaxCrudModal"]/div/div/div[3]/button')
    getCancelOrder_loc = (By.XPATH, '//*[@id="figure1"]/span')
    modifyInformation_loc = (By.XPATH, '//*[@id="w4"]/div[1]/div/div[2]/div/a[3]')
    getOrderType_loc = (By.XPATH, '//*[@id="w4"]/div[2]/div/div[2]/span')
    getOrderType2_loc = (By.ID, 'select2-ordercreateform-type-container')
    remark_loc = (By.ID, 'ordercreateform-remark')
    getRemark_loc = (By.XPATH, '//*[@id="w4"]/div[2]/div/div[12]/span')
    clickSaves_loc = (By.XPATH, '//*[@id="ajaxCrudModal"]/div/div/div[3]/button')
    appointmentTime_loc = (By.XPATH, '//*[@id="w4"]/div[2]/div/div[6]/span')
    clickAppointmentTime_loc = (By.XPATH, '//*[@id="w4"]/div[1]/div/div[2]/div/a[4]')
    inputTime_loc = (By.ID, 'orderappointmentform-appointment_time')
    inputReasonAbout_loc = (By.ID, 'orderappointmentform-orderprogressremark')
    error_loc = (By.XPATH, '//*[@id="order-form"]/div[2]/div/div/div')
    otherTime_loc = (By.XPATH, '//*[@id="w4"]/div[1]/div/div[2]/div/a[6]')
    label_loc = (By.XPATH, '//*[@id="w4"]/div[2]/div/div[10]/span')
    # clickAdd_loc = (By.XPATH, '//*[@id="w10"]/div[1]/div/div[2]/div/a')
    clickSubmitOrder_loc = (By.XPATH, '//*[@id="w4"]/div[1]/div/div[2]/div/a[1]')
    submitted_loc = (By.XPATH, '//*[@id="w0"]/div[2]/div/div[4]/div[1]/span')

    def DetailsPage(self):          # 进入订单详情页面
        self.Management()
        self.another_list()
        self.findElement(*self.confirm_loc).click()
        time.sleep(2)

    def clickSubmitOrders(self):         # 提交订单
        self.findElement(*self.submitOrders_loc).click()
        self.findElement(*self.Save_loc).click()
        time.sleep(2)
        jbg = self.findElement(*self.getSubmitOrders_loc).text
        return jbg

    def clickCancelOrder(self):         # 取消订单
        self.findElement(*self.CancelOrder_loc).click()
        self.findElement(*self.SaveCancelOrder_loc).click()
        ffb = self.findElement(*self.getCancelOrder_loc).text
        return ffb

    def clickModifyInformation(self):       # 点击修改信息
        self.findElement(*self.modifyInformation_loc).click()

    def save(self):       # 点击保存按钮
        self.findElement(*self.clickSaves_loc).click()

    def AppointmentTime(self):      # 点击修改预约时间
        self.findElement(*self.clickAppointmentTime_loc).click()

    def ReasonAbout(self):      # 改约原因
        self.findElement(*self.inputReasonAbout_loc).send_keys('测试')

    def modifyInformation(self):        # 点击修改信息并返回断言信息
        self.clickModifyInformation()
        time.sleep(2)
        fgb = self.findElement(*self.getOrderType_loc).text
        hgb = self.findElement(*self.getOrderType2_loc).get_attribute('title')
        return fgb, hgb

    def SuccessModify(self):        # 修改信息
        self.clickModifyInformation()
        kli = self.findElement(*self.getRemark_loc).text
        self.findElement(*self.remark_loc).clear()
        Time = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:%S')  # 现在时间加一分钟
        self.findElement(*self.remark_loc).send_keys(Time)
        self.save()         # 点击保存
        time.sleep(2)
        oli = self.findElement(*self.getRemark_loc).text
        return kli, oli

    def ChangeTime(self):       # 修改预约时间
        self.AppointmentTime()
        jy = self.findElement(*self.appointmentTime_loc).text
        Time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')  # 现在时间加一天
        self.findElement(*self.inputTime_loc).clear()
        self.findElement(*self.inputTime_loc).send_keys(Time)
        self.ReasonAbout()
        time.sleep(2)
        self.save()
        time.sleep(2)
        br = self.findElement(*self.appointmentTime_loc).text
        return jy, br

    def non_null(self):     # 必填项验证（改约原因）
        self.AppointmentTime()
        self.save()
        hg = self.findElement(*self.error_loc).text
        return hg

    def clickotherTime(self):        # 点击设置长期另约
        dfd = self.findElement(*self.label_loc).text
        self.findElement(*self.otherTime_loc).click()
        time.sleep(2)
        dfs = self.findElement(*self.label_loc).text
        return dfd, dfs

    def clickSubmitOrder(self):     # 点击提交订单
        self.findElement(*self.clickSubmitOrder_loc).click()
        self.save()
        time.sleep(2)
        mjn = self.findElement(*self.submitted_loc).text
        return mjn






