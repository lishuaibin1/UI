# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 11:21
# @Author  : Mr.Li

from page.init import *
from page.Order_details import *

class duplicateOrder(Init, Order):

    def test_SubmitOrders_001(self):
        '''验证提交订单按钮'''
        self.DetailsPage()      # 进入订单详情页面
        jbg = self.clickSubmitOrders()       # 提交订单
        self.assertEqual(jbg, '已提交')

    def test_CancelOrder_002(self):
        '''验证取消订单按钮'''
        self.DetailsPage()      # 进入订单详情页面
        ffb = self.clickCancelOrder()     # 点击取消订单
        self.assertEqual(ffb, '已取消')

    def test_modifyInformation_003(self):
        '''验证修改信息按钮'''
        self.DetailsPage()      # 进入订单详情页面
        fgb, hgb = self.modifyInformation()     # 点击修改信息
        self.assertEqual(fgb, hgb)

    def test_SuccessModify_004(self):
        '''验证成功修改信息'''
        self.DetailsPage()      # 进入订单详情页面
        bgb, fbg = self.SuccessModify()        # 修改信息
        self.assertNotEqual(bgb, fbg)

    def test_ChangeTime_005(self):
        '''修改预约时间'''
        self.DetailsPage()      # 进入订单详情页面
        jy, br = self.ChangeTime()      # 修改预约时间
        self.assertNotEqual(jy, br)

    def test_required_006(self):
        '''验证改约原因为必填项'''
        self.DetailsPage()      # 进入订单详情页面
        jh = self.non_null()
        self.assertEqual(jh, '请填写改约原因')

    def test_otherTime_007(self):
        '''验证设置长期另约按钮'''
        self.DetailsPage()      # 进入订单详情页面
        dfd, dfs = self.clickotherTime()
        self.assertNotEqual(dfd, dfs)

    def test_confirmation_008(self):
        '''验证下单成功'''
        self.DetailsPage()      # 进入订单详情页面
        ngf = self.clickSubmitOrder()
        self.assertEqual(ngf, '已提交')


if __name__ == '__main__':
    unittest.main(verbosity=2)
