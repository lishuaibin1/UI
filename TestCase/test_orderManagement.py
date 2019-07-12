# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 10:31
# @Author  : Mr.Li


from page.init import *
from page.read_file import *

class Order_Management(Init, read):

    def test_Order_list_001(self):
        '''进入订单管理页面'''
        self.Management()
        time.sleep(2)
        dff = self.driver.find_element_by_class_name('panel-title').text
        self.assertEqual(dff, '订单列表')

    def test_search_for_002(self):
        '''验证订单列表页面搜索'''
        self.Management()
        temp = self.read_file2('Order_inquiry')      # 读取json文件数据
        # 获取参数
        a = temp['xiadanshijian']
        b = temp['yuyueshijian']
        c = temp['wanchengshijian']
        d = temp['shebeihao']
        e = temp['chejia']
        f = temp['quyu']
        g = temp['chanpinleixing']
        h = temp['duijieID']
        i = temp['dingdanzhuangtai']
        j = temp['dingdanleixing']
        k = temp['shiwuleixing']
        self.Order_search(a, b, c, d, e, f, g, h, i, j, k)   # 订单搜索输入信息
        self.Search()   # 点击搜索
        time.sleep(2)
        t = self.driver.find_element_by_xpath('//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[6]/p[1]').text
        t1 = t.split(' ')[1]    # 按空格拆分
        # print(t1,type(t1))
        # print(timeArray)
        # print(timeArray.tm_year)    # 2019
        timeStamp = time.mktime(time.strptime(t1, "%Y-%m-%d"))    # 下单时间戳。  time.strptime转换成 "%Y-%m-%d"格式
        # print(timeStamp)
        t2 = a.split(' ')[0]
        t3 = a.split(' ')[2]
        timeStamp2 = time.mktime(time.strptime(t2, "%Y-%m-%d"))
        timeStamp3 = time.mktime(time.strptime(t3, "%Y-%m-%d"))
        if timeStamp >= timeStamp2 and timeStamp<=timeStamp3:
            pass
            # print('通过')
        else:
            print('不通过')

    def test_Order_number_003(self):
        '''验证按订单编号查询'''
        self.Management()
        wqe = self.read_file2('Order_list')
        order_number = wqe['Order_number']
        self.input_number(order_number)   # 输入编号
        time.sleep(2)
        self.enter()
        time.sleep(2)
        bh = self.driver.find_element_by_xpath('//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[2]/p[1]/a').text
        self.assertEqual(bh, order_number)

    def test_Technician_004(self):
        '''验证按技师搜索订单'''
        self.Management()
        wqe = self.read_file2('Order_list')
        technician = wqe['technician']
        self.selection_technician(technician)  # 选择技师
        time.sleep(2)
        self.enter()
        time.sleep(2)
        qwe = self.driver.find_element_by_xpath('//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[3]/p[2]').text
        qwer = qwe.split(' ')[1]
        # print(qwer)
        self.assertEqual(qwer, technician)

    def test_address_005(self):
        '''通过地址搜索订单'''
        self.Management()
        wqe = self.read_file2('Order_list')
        detailed_address = wqe['Detailed_address']
        self.Input_address(detailed_address)   # 输入地址
        self.enter()
        time.sleep(2)
        ff = self.driver.find_element_by_xpath('//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[4]/div').text
        ffs = ff.split()[0]
        # print(ffs)
        self.assertEqual(ffs, detailed_address)

    def test_Customers_006(self):
        '''按客户查询订单'''
        self.Management()
        ewqe = self.read_file2('Order_list')
        customer = ewqe['Customer']
        self.input_customer(customer)      # 输入选择客户
        time.sleep(2)
        self.enter()
        time.sleep(2)
        df = self.driver.find_element_by_xpath('//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[5]/a').text
        dg = df.split('(')[0]
        # print(dg)
        self.assertEqual(dg, customer)

    def test_inquire_007(self):
        '''组合查询'''
        self.Management()
        temp = self.read_file2('Order_list')
        order_number = temp['Order_number']
        technician = temp['technician']
        Detailed_address = temp['Detailed_address']
        customer = temp['Customer']
        self.selection_technician(technician)      # 选择技师
        time.sleep(2)
        self.input_customer(customer)     # 输入选择客户
        time.sleep(2)
        self.input_number(order_number)     # 输入编号
        self.Input_address(Detailed_address)        # 输入详细地址
        time.sleep(2)
        self.enter()     # 回车点击空白地方
        time.sleep(2)
        df = self.driver.find_element_by_xpath('//*[@id="crud-datatable-container"]/table/tbody/tr[1]/td[5]/a').text
        dg = df.split('(')[0]
        # print(dg)
        self.assertEqual(dg, customer)

    def test_order_details_008(self):
        '''查看订单详情页面'''
        self.Management()       # 进入订单列表页面
        ngr = self.entry_order_details()      # 点击订单编号进入订单详情页面,返回页面关键信息赋值给ngr
        self.assertEqual(ngr, '强改状态')

    def test_customer_information_009(self):
        '''查看客户信息'''
        self.Management()      # 进入订单列表页面
        nj, ayls = self.customer_details()       # 点击客户查看客户详细信息,返回页面关键信息赋值给nj, ayls
        self.assertEqual(nj, ayls)     # 点击查询的客户名称与查询到的客户名称一致

    def test_close_Windows_010(self):
        '''关闭客户详情信息弹窗'''
        self.Management()  # 进入订单列表页面
        self.customer_details()  # 点击客户查看客户详细信息
        time.sleep(2)
        dff = self.clickClose()       # 点击客户详情弹框关闭图标并返回页面关键信息赋值给dff
        self.assertEqual(dff, '订单列表')

    def test_affair_011(self):
        '''查看事务'''
        self.Management()     # 进入订单列表页面
        wqe = self.read_file2('Order_list')
        order_number = wqe['Order_number']
        self.input_number(order_number)   # 输入编号
        time.sleep(2)
        self.enter()
        time.sleep(2)
        mzz, hb = self.affair()       # 把返回的mzz, hb页面信息赋值给mzz, hb
        self.assertEqual(mzz, hb)

    def test_Register_complaints_012(self):
        '''验证登记投诉按钮'''
        self.Management()     # 进去订单管理页面
        tq = self.register_complaints()        # 点击登录投诉按钮
        self.assertEqual(tq, '投诉人姓名')

    def test_Another_list_013(self):
        '''验证再来一单按钮'''
        self.Management()      # 进去订单管理页面
        gdv = self.another_list()       # 点击再来一单按钮
        # print(gdv)
        self.assertEqual(gdv, '再来一单')

    def test_follow_up_o14(self):
        '''验证跟进按钮'''
        self.Management()     # 进去订单管理页面
        njh = self.follow_up()      # 点击跟进按钮
        self.assertEqual(njh, '跟进')

    def test_Add_order_015(self):
        '''验证新建订单按钮'''
        self.Management()     # 进去订单管理页面
        kyh = self.new_order()      # 点击新建订单
        self.assertEqual(kyh, '客户')

    def test_skip_016(self):
        '''验证切换页面功能'''
        self.Management()     # 进去订单管理页面
        self.pagedView()      # 向下滑动页面  直接滑动到底
        time.sleep(2)
        jhg = self.skip()       # 点击下一页按钮并返回页面关键信息复制给jhg
        self.assertEqual(jhg, '21-40')


if __name__ == '__main__':
    unittest.main(verbosity=2)
