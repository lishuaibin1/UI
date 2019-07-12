# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 16:25
# @Author  : Mr.Li

from page.init import *
from page.dingdan import *
from page.newOrder import *
from page.read_file import *
from string import Template

class NewOrder(Init, newOrder):

    def test_customerChoice_001(self):
        '''验证客户选择下拉框'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        ewqe = self.read_file1()
        customer = ewqe['Customer']
        lp = self.Input_customer(customer)
        time.sleep(2)
        self.assertEqual(lp, '李帅宾')

    def test_orderAccount_002(self):
        '''验证下单账号的选择'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        ewqe = self.read_file1()
        customer = ewqe['Customer']
        Order_account = ewqe['Order_account']
        self.Input_customer(customer)       # 选择客户
        trh = self.order_account(Order_account)     # 选择下拉账号
        time.sleep(2)
        self.assertEqual(trh, Order_account)

    def test_appointmentTime_003(self):
        '''选择预约时间'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        lpl, dfv = self.appointment_time()        # lpl获取到的时间，dfv输入的时间
        time.sleep(2)
        self.assertEqual(lpl, dfv)

    def test_linkman_004(self):
        '''输入现场联系人'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        nmk = self.read_file1()      # 读取json文件
        Contacts = nmk['Contacts']
        self.linkman(Contacts)
        time.sleep(2)

    def test_OrderType_005(self):
        '''验证订单类型选择下拉框'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        hfgh = self.read_file1()         # 读取json文件
        ghn = hfgh['order_type']
        bhf = self.OrderType(ghn)
        time.sleep(2)
        self.assertEqual(bhf, ghn)

    def test_province_006(self):
        '''验证省选择下拉框'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        fjj = self.province()       # 选择省
        time.sleep(2)
        self.assertEqual(fjj, '2801')

    def test_city_007(self):
        '''验证选择市下拉框'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        self.province()       # 选择省
        ujj = self.city()       # 选择市
        time.sleep(2)
        self.assertEqual(ujj, '2802')

    def test_area_008(self):
        '''验证区选择下拉框'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        self.province()       # 选择省
        self.city()           # 选择市
        jmy = self.area()
        time.sleep(2)
        self.assertEqual(jmy, '2808')

    def test_customerRequired_009(self):
        '''验证客户为必填项'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        self.appointment_time()       # 输入预约时间
        uyf = self.read_file1()      # 读取json文件
        contacts = uyf['Contacts']
        Telephone = uyf['Telephone']
        Reservation_address = uyf['Reservation_address']
        order_type = uyf['order_type']
        self.OrderType(order_type)      # 传参输入订单类型
        self.not_required(contacts, Telephone, Reservation_address)     # 传参输入其他非必填项
        self.province()       # 选择省
        self.city()       # 选择市
        self.area()       # 选择区
        self.save()       # 点击保存按钮
        time.sleep(2)
        fbd = self.customerRequired()
        self.assertEqual(fbd, '客户不能为空。')

    def test_AccountRequired_010(self):
        '''验证下单账号必填'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        ewqe = self.read_file1()
        customer = ewqe['Customer']
        order_type = ewqe['order_type']
        self.Input_customer(customer)
        self.OrderType(order_type)      # 传参输入订单类型
        self.save()       # 点击保存按钮
        time.sleep(2)
        ggh = self.AccountRequired()
        self.assertEqual(ggh, '下单账号不能为空。')

    def test_typeRequired_011(self):
        '''验证订单类型必填项'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        ewqe = self.read_file1()
        customer = ewqe['Customer']
        Order_account = ewqe['Order_account']
        self.Input_customer(customer)
        self.order_account(Order_account)
        self.save()       # 点击保存按钮
        time.sleep(2)
        fhjn = self.typeRequired()
        self.assertEqual(fhjn, '订单类型不能为空。')

    def test_saveOrder_012(self):
        '''验证下单成功'''
        self.Management()     # 进入订单管理页面
        self.new_order()      # 点击新建订单
        time = self.SuccessfulOrder()
        fdf = self.OrderSucceed()
        # nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在时间
        # ghht = fdf.split('\n')
        # # print(ghht,'\n',nowTime)
        # htnf = Template('${s1} ${s2}')      # 拼接时间戳
        # fgg = htnf.safe_substitute(s1=ghht[0], s2=ghht[1])
        # # print(fgg)
        self.assertEqual(time, fdf)

    def test_addCar_013(self):
        '''验证添加车辆'''
        self.Management()       # 进入订单管理页面
        self.new_order()        # 点击新建订单
        self.SuccessfulOrder()      # 新建订单输入信息
        hngn = self.AddCar()        # 添加车辆
        self.assertEqual(hngn, '施工车辆 ( 1 辆 )')

    def test_AddProduct_014(self):
        '''验证添加产品'''
        self.Management()       # 进入订单管理页面
        self.new_order()        # 点击新建订单
        self.SuccessfulOrder()      # 新建订单输入信息
        time.sleep(2)
        self.AddCar()
        time.sleep(2)
        hj = self.addProduct()
        self.assertEqual(hj, '服务清单 ( 2 )')


