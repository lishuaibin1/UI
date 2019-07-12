# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 16:56
# @Author  : Mr.Li

from page.login import login
from selenium.webdriver.common.by import By
import time
import os

class OrderManagement(login):

    ClickOrderManagement_loc = (By.CLASS_NAME, 'dropdown-toggle')
    ClickOrderList_loc = (By.LINK_TEXT, '订单列表')
    clickSearch_loc = (By.XPATH, '//*[@id="w0"]/div/div[12]/button')
    createTime_loc = (By.ID, 'ordersearch-create_time')
    updateTime_loc = (By.ID, 'ordersearch-appointment_time')
    completeTime_loc = (By.ID, 'ordersearch-update_time')
    deviceNo_loc = (By.ID, 'ordersearch-driver_number')
    frameNumber_loc = (By.ID, 'ordersearch-car_search_info')
    region_loc = (By.ID, 'select2-ordersearch-district-container')
    input_loc = (By.XPATH, '/html/body/span/span/span[1]/input')
    productType_loc = (By.ID, 'select2-ordersearch-product_type-container')
    dockingIDPath_loc = (By.ID, 'ordersearch-unique_id')
    orderStatusPath_loc = (By.ID, 'select2-ordersearch-status-container')
    orderTypePath_loc = (By.ID, 'select2-ordersearch-type-container')
    transactionTypePath_loc = (By.ID, 'select2-ordersearch-work_type-container')
    selectTechnicianPath_loc = (By.ID, 'select2-ordersearch-engineer_id-container')
    clickTechnicianPath_loc = (By.XPATH, '//*[@id="select2-ordersearch-engineer_id-results"]/li')
    enterPath_loc = (By.CLASS_NAME, 'panel-title')
    inputNumberPath_loc = (By.NAME, 'OrderSearch[code]')
    InputAddressPath_loc = (By.NAME, 'OrderSearch[address_full]')
    clickCustomerPath_loc = (By.ID, 'select2-ordersearch-customer_id-container')
    ChoiceCustomerPath_loc = (By.XPATH, '//*[@id="select2-ordersearch-customer_id-results"]/li')
    entryOrderDetailsPath_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[2]/p[1]/a')
    GetKeywordPath1_loc = (By.CSS_SELECTOR, '#w4 > div.panel-heading > div > div:nth-child(2) > div > a:nth-child(5)')
    CustomerPath_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[5]/a')
    CustomerInformationPath_loc = (By.XPATH, '//*[@id="w0"]/tbody/tr[1]/td')
    CloseIconPath_loc = (By.CLASS_NAME, 'close')
    GetKeywordPath2_loc = (By.CLASS_NAME, 'panel-title')
    TransactionJumpPath_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr/td[8]/div/a')
    TransactionKeywordsPath_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr/td[10]')
    ComplaintPath_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[10]/a[1]')
    complaintKeywordPath_loc = (By.XPATH, '//*[@id="customer-form"]/div[1]/label')
    DuplicateOrdersPath_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[10]/a[2]')
    AnotherSingleKeyword_loc = (By.CLASS_NAME, 'modal-title')
    FollowUpPath_loc = (By.XPATH, '//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[10]/a[3]')
    followUpKeyword_loc = (By.XPATH, '//*[@id="ajaxCrudModal"]/div/div/div[1]/h4')
    newOrderPath_los = (By.XPATH, '//*[@id="uzh-toolbar"]/div[2]/div/a[1]')
    newOrderKW_los = (By.XPATH, '//*[@id="order-form"]/div[1]/div[1]/div/label')
    skipPath_loc = (By.XPATH, '//*[@id="crud-datatable"]/div/div[6]/div[1]/ul/li[12]/a')
    skipKwPath_loc = (By.XPATH, '//*[@id="crud-datatable"]/div/div[1]/div[1]/div/b[1]')

    def path(self, file='Config', filename=None):
        '''
        :param file: 文件夹
        :param filename: 文件名字
        :return:json文件路径
        '''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), file, filename)
        # json_path = 'D:\\pycharm工程\\uzhyyd\\Config\\dingdanliebiao.json'  # 文件路径
        # return json_path

    def ClickOrderManagement(self):
        '''点击订单管理'''
        self.findElement(*self.ClickOrderManagement_loc).click()

    def ClickOrderList(self):
        '''点击订单列表'''
        self.findElement(*self.ClickOrderList_loc).click()

    def Search(self):
        '''点击搜索'''
        self.findElement(*self.clickSearch_loc).click()

    def create_time(self, order_time):
        '''下单时间'''
        self.findElement(*self.createTime_loc).send_keys(order_time)

    def updateTime(self, update_time):
        '''预约时间'''
        self.findElement(*self.updateTime_loc).send_keys(update_time)

    def completeTime(self, complete_time):
        '''完成时间'''
        self.findElement(*self.completeTime_loc).send_keys(complete_time)

    def device_no(self, device_no):
        '''输入设备编号'''
        self.findElement(*self.deviceNo_loc).send_keys(device_no)

    def frameNumber(self, frame_number):
        '''输入车架号'''
        self.findElement(*self.frameNumber_loc).send_keys(frame_number)

    def Choice_Region(self, region):
        '''选择区域'''
        self.findElement(*self.region_loc).click()
        self.findElement(*self.input_loc).send_keys(region)

    def product_type(self, product_type):
        '''选择产品类型'''
        self.findElement(*self.productType_loc).click()
        self.findElement(*self.input_loc).send_keys(product_type)

    def dockingID(self, dockingID):
        '''对接ID'''
        self.findElement(*self.dockingIDPath_loc).send_keys(dockingID)

    def orderStatus(self, order_status):
        '''订单状态'''
        self.findElement(*self.orderStatusPath_loc).click()
        self.findElement(*self.input_loc).send_keys(order_status)

    def orderType(self, order_type):
        '''订单类型'''
        self.findElement(*self.orderTypePath_loc).click()
        self.findElement(*self.input_loc).send_keys(order_type)

    def transactionType(self, transaction_type):
        '''事务类型'''
        self.findElement(*self.transactionTypePath_loc).click()
        self.findElement(*self.input_loc).send_keys(transaction_type)

    def enter(self):      # 回车
        self.findElement(*self.enterPath_loc).click()

    def Management(self):   # 进入订单管理页面
        self.Logins()
        self.ClickOrderManagement()
        self.ClickOrderList()

    def Order_search(self,order_time,appointment,complete_time, device_no,frame_number,region,product_type,
                    dockingID,order_status,order_type, transaction_type):   # 订单搜索输入信息
        '''
        :param driver:
        :param order_time: 下单时间
        :param appointment: 预约时间
        :param complete_time: 完成时间
        :param device_no: 设备号
        :param frame_number: 车架号
        :param region: 区域
        :param product_type: 产品类型
        :param dockingID:对接ID
        :param order_status:订单状态
        :param order_type:订单类型
        :param transaction_type:事务类型
        :return:
        '''
        self.create_time(order_time)    # 下单时间
        time.sleep(2)
        self.updateTime(appointment)    # 预约时间
        time.sleep(2)
        self.completeTime(complete_time)     # 完成时间
        time.sleep(2)
        self.device_no(device_no)    # 设备号
        time.sleep(2)
        self.frameNumber(frame_number)   # 车架号
        time.sleep(2)
        self.Choice_Region(region)   # 输入区域
        time.sleep(2)
        self.product_type(product_type)  # 输入产品类型
        time.sleep(2)
        self.dockingID(dockingID)  # 对接ID
        time.sleep(2)
        self.orderStatus(order_status)  # 订单状态
        time.sleep(2)
        self.orderType(order_type)  # 订单类型
        time.sleep(2)
        self.transactionType(transaction_type)  # 事务类型

    def selection_technician(self, technician):     # 选择技师
        self.findElement(*self.selectTechnicianPath_loc).click()
        self.findElement(*self.input_loc).send_keys(technician)
        time.sleep(2)
        self.findElement(*self.clickTechnicianPath_loc).click()

    def input_number(self, order_number):
        '''输入编号'''
        self.findElement(*self.inputNumberPath_loc).send_keys(order_number)

    def Input_address(self, Detailed_address):
        '''输入详细地址'''
        self.findElement(*self.InputAddressPath_loc).send_keys(Detailed_address)

    def input_customer(self, customer):    # 输入选择客户
        self.findElement(*self.clickCustomerPath_loc).click()
        self.findElement(*self.input_loc).send_keys(customer)
        time.sleep(2)
        self.findElement(*self.ChoiceCustomerPath_loc).click()

    def entry_order_details(self):        # 进入订单详情页面,返回页面关键信息
        self.findElement(*self.entryOrderDetailsPath_loc).click()
        time.sleep(2)
        AllHandles = self.driver.window_handles  # 获取全部页面句柄
        self.driver.switch_to_window(AllHandles[1])  # 切换页面
        ngr = self.findElement(*self.GetKeywordPath1_loc).text
        return ngr

    def customer_details(self):        # 点击客户查看客户详细信息并返回页面关键信息
        vn = self.findElement(*self.CustomerPath_loc).text  # 获取查询路径的客户信息
        nj = vn.split('(')[0]  # 按'('分离数据
        self.findElement(*self.CustomerPath_loc).click()
        time.sleep(2)
        lzm = self.findElement(*self.CustomerInformationPath_loc).text
        ayls = lzm.split('(')[0]
        return nj, ayls

    def clickClose(self):     # 点击客户详情弹框关闭图标并返回页面关键信息
        self.findElement(*self.CloseIconPath_loc).click()  # 点击关闭图标
        time.sleep(2)
        dff = self.findElement(*self.GetKeywordPath2_loc).text
        return dff

    def affair(self):     # 点击查看事物并返回页面关键信息
        hbs = self.findElement(*self.TransactionJumpPath_loc).text  # 获取查询路径的事务类型
        mzzw = hbs.split('(')[0]
        self.findElement(*self.TransactionJumpPath_loc).click()  # 点击事务
        time.sleep(2)
        hb = self.findElement(*self.TransactionKeywordsPath_loc).text  # 获取查询结果的事务类型
        return mzzw, hb

    def register_complaints(self):        # 点击登录投诉按钮并返回页面关键信息
        self.findElement(*self.ComplaintPath_loc).click()
        time.sleep(2)
        tq = self.findElement(*self.complaintKeywordPath_loc).text
        return tq

    def another_list(self):       # 点击再来一单按钮并返回页面关键信息
        self.findElement(*self.DuplicateOrdersPath_loc).click()
        time.sleep(2)
        gdv = self.findElement(*self.AnotherSingleKeyword_loc).text
        return gdv

    def follow_up(self):      # 点击跟进按钮并返回页面关键信息
        self.findElement(*self.FollowUpPath_loc).click()
        time.sleep(2)
        njh = self.findElement(*self.followUpKeyword_loc).text
        return njh

    def new_order(self):      # 点击新建订单并返回页面内关键信息
        self.findElement(*self.newOrderPath_los).click()
        time.sleep(2)
        kyh = self.findElement(*self.newOrderKW_los).text
        return kyh

    def pagedView(self):      # 向下滑动页面  滑动到底部
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # def upglide(self):      # 向上滑动页面
    #     self.driver.execute_script("window.scrollTo(0,-2000)")

    def skip(self):       # 点击下一页按钮
        self.findElement(*self.skipPath_loc).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,-2000)")       # 向上滑动页面
        jhg = self.findElement(*self.skipKwPath_loc).text   # 获取页面关键信息
        return jhg



