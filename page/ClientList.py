# -*- coding: utf-8 -*-
# @Time    : 2019/6/15 11:09
# @Author  : Mr.Li

from page.login import *
from selenium.webdriver.common.keys import Keys
import time as t
from page.read_file import *
from selenium.webdriver.support.select import Select

class ClientManagement(read):
    clickClientManagement_loc = (By.XPATH, '//*[@id="w1"]/li[2]/a')
    clickClientList_loc = (By.XPATH, '//*[@id="w3"]/li/a')
    clickEditInformation_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[17]/a[1]')
    TradeName_loc = (By.XPATH, '//*[@id="crud-datatable-filters"]/td[2]/input')
    getTradeName_loc = (By.ID, 'customerform-name')
    IDInquire_loc = (By.XPATH, '//*[@id="crud-datatable-filters"]/td[1]/input')
    getID_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr/td[3]')
    character_loc = (By.ID, 'select2-customersearch-type-container')
    character2_loc = (By.ID, 'select2-customersearch-type-results')
    getCharacter_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[5]')
    linkman_loc = (By.NAME, 'CustomerSearch[contact]')
    phone_loc = (By.NAME, 'CustomerSearch[phone]')
    getLinkman_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr/td[6]')
    getPhone_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr/td[7]')
    approvalStatus_loc = (By.ID, 'select2-customersearch-status-container')
    approvalStatus2_loc = (By.ID, 'select2-customersearch-status-results')
    getApprovalStatus_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr/td[8]')
    clickCreate_loc = (By.XPATH, '//*[@id="uzh-toolbar"]/div[2]/div/a[1]')
    newTradeName_loc = (By.ID, 'customerform-name')
    province_loc = (By.ID, 'customerform-province')
    city_loc = (By.ID, 'customerform-city')
    area_loc = (By.ID, 'customerform-area')
    role_loc = (By.ID, 'select2-customerform-type-container')
    role2_loc = (By.ID, 'select2-customerform-type-results')
    save2_loc = (By.XPATH, '//*[@id="ajaxCrudModal"]/div/div/div[3]/button')
    getTradeName2_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[4]')
    delete_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[17]/a[2]')


    def ClientList(self):       # 进入客户列表页面
        self.Logins()
        self.findElement(*self.clickClientManagement_loc).click()
        t.sleep(1)
        self.findElement(*self.clickClientList_loc).click()
        t.sleep(1)

    def Enter(self):        # 回车键
        self.findElement(*self.TradeName_loc).send_keys(Keys.ENTER)

    def TradeName(self):        # 企业名称
        wqe = self.read_file3('clientList')
        Trade_Name = wqe['Trade_Name']
        self.findElement(*self.TradeName_loc).send_keys(Trade_Name)
        self.Enter()
        t.sleep(2)

    def clickEditInformation(self):      # 点击编辑客户信息按钮
        self.findElement(*self.clickEditInformation_loc).click()
        t.sleep(2)
        ghv = self.findElement(*self. getTradeName_loc).get_attribute('value')
        return ghv

    def IDinquire(self):        # 输入客户ID
        wqe = self.read_file3('clientList')
        ID = wqe['ID']
        self.findElement(*self.IDInquire_loc).send_keys(ID)
        t.sleep(2)
        self.Enter()
        t.sleep(1)
        htj = self.findElement(*self.getID_loc).text
        return htj, ID

    def character(self):        # 选择角色
        wqe = self.read_file3('clientList')
        vdv = wqe['role']
        self.findElement(*self.character_loc).click()
        t.sleep(1)
        yj = self.findElement(*self.character2_loc)
        hg = yj.find_elements_by_tag_name('li')
        for bk in hg:
            if bk.text == vdv:
                bk.click()
                t.sleep(2)
                break
        ghh = self.findElement(*self.getCharacter_loc).text
        return ghh, vdv

    def inputLinkman(self):      # 输入联系人
        wqe = self.read_file3('clientList')
        vdv = wqe['linkman']
        self.findElement(*self.linkman_loc).send_keys(vdv)
        self.Enter()
        t.sleep(2)
        jg = self.findElement(*self.getLinkman_loc).text
        return jg, vdv

    def inputPhone(self):       # 输入联系电话
        wqe = self.read_file3('clientList')
        dv = wqe['phone']
        self.findElement(*self.phone_loc).send_keys(dv)
        self.Enter()
        t.sleep(2)
        jg = self.findElement(*self.getPhone_loc).text
        return jg, dv

    def approval_status(self):      # 选择审核状态
        wqe = self.read_file3('clientList')
        dv = wqe['approval_status']
        self.findElement(*self.approvalStatus_loc).click()
        t.sleep(2)
        fc = self.findElement(*self.approvalStatus2_loc)
        jhj = fc.find_elements_by_tag_name('li')
        for lol in jhj:
            if lol.text == dv:
                lol.click()
                t.sleep(2)
                break
        cvb = self.findElement(*self.getApprovalStatus_loc).text
        return cvb, dv

    def clickCreate(self):      # 点击新建客户
        self.findElement(*self.clickCreate_loc).click()

    def provinces(self):       # 选择省
        fgj = Select(self.findElement(*self.province_loc))
        fgj.select_by_value('2801')     # 2801陕西省编码

    def citys(self):       # 选择市
        jgfh = Select(self.findElement(*self.city_loc))
        jgfh.select_by_value('2802')        # 西安市编码

    def areas(self):       # 选择区
        fb = Select(self.findElement(*self.area_loc))
        fb.select_by_visible_text('雁塔区')

    def role(self):        # 新建客户选择角色
        self.findElement(*self.role_loc).click()
        t.sleep(1)
        yj = self.findElement(*self.role2_loc)
        hg = yj.find_elements_by_tag_name('li')
        for bk in hg:
            if bk.text == '天易子客户':
                bk.click()
                t.sleep(2)
                break

    def save2(self):        # 保存
        self.findElement(*self.save2_loc).click()

    def CreateCustomer(self):       # 创建客户
        self.clickCreate()
        t.sleep(1)
        self.findElement(*self.newTradeName_loc).send_keys('用测试')
        t.sleep(1)
        self.provinces()
        self.citys()
        self.areas()
        t.sleep(1)
        self.role()
        self.save2()
        t.sleep(2)
        ghv = self.findElement(*self.getTradeName2_loc).text
        return ghv

    def delete(self):       # 删除客户
        hg = self.findElement(*self.getID_loc).text
        self.findElement(*self.delete_loc).click()
        self.save2()
        t.sleep(2)
        jm = self.findElement(*self.getID_loc).text
        return hg, jm

