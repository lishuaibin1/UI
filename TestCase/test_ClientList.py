# -*- coding: utf-8 -*-
# @Time    : 2019/6/15 11:10
# @Author  : Mr.Li


from page.init import *
from page.ClientList import *


class clientList(Init, ClientManagement):

    def test_EnterCustomerList_001(self):
        '''验证编辑客户信息按钮'''
        self.ClientList()       # 进入客户列表页面
        self.TradeName()        # 按企业名称查询
        dsf = self.clickEditInformation()     # 点击编辑客户信息按钮
        self.assertEqual(dsf, '李帅宾')

    def test_idInquire_002(self):
        '''验证通过ID查找客户'''
        self.ClientList()       # 进入客户列表页面
        htj, ID = self.IDinquire()        # 输入ID
        self.assertEqual(htj, ID)

    def test_character_003(self):
        """验证按角色查询客户信息"""
        self.ClientList()       # 进入客户列表页面
        mhm, vdv = self.character()     # 选择角色
        self.assertEqual(mhm, vdv)

    def test_linkman_004(self):
        """验证按联系人查询客户信息"""
        self.ClientList()       # 进入客户列表页面
        jg, vdv = self.inputLinkman()       # 输入联系人
        self.assertEqual(jg, vdv)

    def test_phone_005(self):
        """验证按联系电话查询客户信息"""
        self.ClientList()       # 进入客户列表页面
        jg, vdv = self.inputPhone()         # 输入联系电话
        self.assertEqual(jg, vdv)

    def test_approvalStatus_006(self):
        """验证按审批状态查询客户信息"""
        self.ClientList()       # 进入客户列表页面
        cvb, dv = self.approval_status()        # 选择审核状态
        self.assertEqual(cvb, dv)

    def test_CreateCustomer_007(self):
        """验证创建新客户"""
        self.ClientList()       # 进入客户列表页面
        jy = self.CreateCustomer()      # 输入新建客户信息
        self.assertEqual(jy, '用测试')

    def test_delete_008(self):
        """验证删除客户"""
        self.ClientList()       # 进入客户列表页面
        hg, jm = self.delete()      # 删除客户
        self.assertNotEqual(hg, jm)

