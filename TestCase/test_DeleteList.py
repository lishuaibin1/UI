# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 11:14
# @Author  : Mr.Li

from page.DeleteList import *
from page.init import *



class MyTestCase(Init,delete):

    def test_deleteList_001(self):
        """进入删除列表页面"""
        a = self.enterDeleteList()
        self.assertNotEqual(a, '删除列表')

    def test_EquipmentEmpty_002(self):
        """验证删除设备号为空"""
        self.enterDeleteList()      # 进入设备删除列表页面
        b = self.EquipmentEmpty()
        self.assertEqual(b, '设备号不能为空。')

    def test_InputDeviceNumber_003(self):
        """验证输入不在库设备号"""
        self.enterDeleteList()      # 进入设备删除列表页面
        c = self.InputDeviceNumber()        # 输入设备号不在库
        self.assertEqual(c, '设备不在库')

    def test_DeleteReason_004(self):
        """验证删除原因下拉框"""
        self.enterDeleteList()      # 进入设备删除列表页面
        g = self.deleteReason()
        self.assertEqual(g, '回收报废')

    def test_UsedEquipment_005(self):
        """验证已使用的设备删除不成功"""
        self.enterDeleteList()      # 进入设备删除列表页面



if __name__ == '__main__':
    unittest.main()
