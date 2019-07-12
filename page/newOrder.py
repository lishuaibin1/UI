# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 16:29
# @Author  : Mr.Li

from page.ComboBox import *
import datetime
from selenium.webdriver.support.select import Select
from base.base import *
from selenium.webdriver.common.by import By
from page.read_file import *


class newOrder(read):
    getCustomer_loc = (By.XPATH, '//*[@id="order-form"]/div[1]/div[1]/div/span/span[1]/span')
    getAccount_loc = (By.XPATH, '//*[@id="select2-ordercreateform-customer_user_id-container"]')
    appointmentTime_loc = (By.ID, 'ordercreateform-appointment_time')
    FieldContact_loc = (By.ID, 'ordercreateform-contact')
    getAppointmentTime_loc = (By.ID, 'ordercreateform-appointment_time')
    clickSave_loc = (By.XPATH, '//*[@id="ajaxCrudModal"]/div/div/div[3]/button')
    getOrderType_loc = (By.ID, 'select2-ordercreateform-type-container')
    province_loc = (By.ID, 'ordercreateform-province')
    city_loc = (By.ID, 'ordercreateform-city')
    area_loc = (By.ID, 'ordercreateform-area')
    phone_loc = (By.ID, 'ordercreateform-phone')
    address_loc = (By.ID, 'ordercreateform-address')
    getCustomerRequired_loc = (By.XPATH, '//*[@id="order-form"]/div[1]/div[1]/div/div')
    getAccountRequired_loc = (By.XPATH, '//*[@id="order-form"]/div[1]/div[2]/div/div')
    getTypeRequired_loc = (By.XPATH, '//*[@id="order-form"]/div[3]/div/div/div')
    getOrderSucceed_loc = (By.XPATH, '//*[@id="w4"]/div[2]/div/div[6]/span')
    clickAddCar_loc = (By.XPATH, '//*[@id="w10"]/div[1]/div/div[2]/div/a')
    ConstructionVehicles_loc = (By.XPATH, '//*[@id="w13"]/div[1]/div/div[1]')
    addProduct_loc = (By.XPATH, '//*[@id="w10"]/div[1]/div/div[2]/div/a[2]')
    ProductType_loc = (By.ID, 'select2-orderproductitemform-product_type-container')
    ProductOptions_loc = (By.XPATH, '//*[@id="select2-orderproductitemform-product_type-results"]')
    productService_loc = (By.ID, 'select2-orderproductitemform-product_id-container')
    ServiceOptions_loc = (By.ID, 'select2-orderproductitemform-product_id-results')
    year_loc = (By.XPATH, '//*[@id="install-schema-preview"]/div/div[1]/select')
    ServiceListing_loc = (By.XPATH, '//*[@id="w14"]/div[1]/div/div[1]/small')



    def Input_customer(self, content):    # 输入选择客户
        content = content
        by_id = 'select2-ordercreateform-customer_id-container'
        by_class = 'select2-search__field'
        by_ids = 'select2-ordercreateform-customer_id-results'
        combobox(self.driver, content, by_id, by_class, by_ids)
        sdfg = self.findElement(*self.getCustomer_loc).text
        nk = sdfg.split('\n')[1]
        return nk

    def order_account(self, content):     # 选择下单账号
        contents = content
        by_id = 'select2-ordercreateform-customer_user_id-container'
        by_class = 'select2-search__field'
        by_ids = 'select2-ordercreateform-customer_user_id-results'
        combobox(self.driver, contents, by_id, by_class, by_ids)      # 调用下拉框方法传参
        hgk = self.findElement(*self.getAccount_loc).text
        jjh = hgk.split('\n')[1]
        return jjh

    def appointment_time(self):       # 输入预约时间
        # nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:00')  # 获取现在时间
        Time = (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:00')  # 未来两小时时间
        # print('\n', nowTime, '\n', Time)
        self.findElement(*self.appointmentTime_loc).clear()
        self.findElement(*self.appointmentTime_loc).send_keys(Time)
        self.findElement(*self.FieldContact_loc).click()
        ojko = self.findElement(*self.getAppointmentTime_loc).get_attribute("value")
        return ojko, Time

    def save(self):       # 点击保存按钮
        self.findElement(*self.clickSave_loc).click()

    def linkman(self, contacts):      # 联系人
        self.findElement(*self.FieldContact_loc).send_keys(contacts)

    def phone(self, Telephone):     # 现场联系电话
        self.findElement(*self.phone_loc).send_keys(Telephone)

    def adress(self, Reservation_address):          # 预约地址
        self.findElement(*self.address_loc).send_keys(Reservation_address)

    def customerRequired(self):         # 获取必填项客户报错信息
        fbd = self.findElement(*self.getCustomerRequired_loc).text
        return fbd

    def AccountRequired(self):          # 获取必填项下单账号报错
        ggh = self.findElement(*self.getAccountRequired_loc).text
        return ggh

    def typeRequired(self):         # 获取必填项订单类型报错信息
        fhjn = self.findElement(*self.getTypeRequired_loc).text
        return fhjn

    def OrderSucceed(self):        # 下单成功页面断言关键信息
        fdf = self.findElement(*self.getOrderSucceed_loc).text
        return fdf

    def OrderType(self, content):      # 选择订单类型
        by_id = 'select2-ordercreateform-type-container'
        by_class = 'select2-search__field'
        by_ids = 'select2-ordercreateform-type-results'
        combobox(self.driver, content, by_id, by_class, by_ids)
        jyh = self.findElement(*self.getOrderType_loc).get_attribute("title")
        return jyh

    def province(self):       # 选择省
        fgj = Select(self.findElement(*self.province_loc))
        fgj.select_by_value('2801')     # 2801陕西省编码
        yjt = self.findElement(*self.province_loc).get_attribute("value")
        return yjt

    def city(self):       # 选择市
        jgfh = Select(self.findElement(*self.city_loc))
        jgfh.select_by_value('2802')        # 西安市编码
        fjn = self.findElement(*self.city_loc).get_attribute("value")
        return fjn

    def area(self):       # 选择区
        fb = Select(self.findElement(*self.area_loc))
        fb.select_by_visible_text('雁塔区')
        fjfgg = self.findElement(*self.area_loc).get_attribute("value")
        return fjfgg

    def not_required(self, Contacts, Telephone, Reservation_address):       # 非必填项的输入
        self.findElement(*self.FieldContact_loc).send_keys(Contacts)
        self.findElement(*self.phone_loc).send_keys(Telephone)
        self.findElement(*self.address_loc).send_keys(Reservation_address)

    def SuccessfulOrder(self):      # 新建订单输入信息
        ewqe = self.read_file1()
        customer = ewqe['Customer']
        Order_account = ewqe['Order_account']
        order_type = ewqe['order_type']
        Telephone = ewqe['Telephone']
        Reservation_address = ewqe['Reservation_address']
        Contacts = ewqe['Contacts']
        self.Input_customer(customer)       # 传参选择客户
        self.order_account(Order_account)       # 传参选择下单账号
        self.OrderType(order_type)          # 传参输入订单类型
        time = self.appointment_time()[0]
        self.province()
        self.city()
        self.area()
        self.not_required(Contacts, Telephone, Reservation_address)         # 输入剩余非必填项
        self.save()
        return time

    def AddCar(self):       # 添加车辆
        self.findElement(*self.clickAddCar_loc).click()
        time.sleep(2)
        self.save()
        time.sleep(2)
        hfn = self.findElement(*self.ConstructionVehicles_loc).text
        return hfn

    def addProduct(self):       # 添加产品
        self.findElement(*self.addProduct_loc).click()          # 点击添加产品按钮
        time.sleep(2)
        self.findElement(*self.ProductType_loc).click()         # 选择产品类型
        time.sleep(2)
        fgc = self.findElement(*self.ProductOptions_loc)
        fdg = fgc.find_elements_by_tag_name('li')
        for fgl in fdg:
            time.sleep(1)
            if fgl.text == '安装GPS-无线':
                fgl.click()
                time.sleep(2)
                break
        self.findElement(*self.productService_loc).click()          # 选择产品服务
        time.sleep(1)
        gf = self.findElement(*self.ServiceOptions_loc)
        hrf = gf.find_elements_by_tag_name('li')
        for ng in hrf:
            time.sleep(1)
            if ng.text == '非带货安装-无线':
                ng.click()
                time.sleep(2)
                break
        uo = Select(self.findElement(*self.year_loc))       # 选择年期
        uo.select_by_value('1年期')
        self.save()
        time.sleep(2)
        hj = self.findElement(*self.ServiceListing_loc).text
        return hj
