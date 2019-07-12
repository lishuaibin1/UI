# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 14:23
# @Author  : Mr.Li

from page.equipmentManagement import *
from page.init import *
import unittest


class EquipmentManagement(Init, equipmentManagement):

    def test_001(self):
        """进入设备管理页面"""
        A = self.enterEquipmentManagement()
        self.assertEqual(A, '设备管理')

    def test_002(self):
        """"""



if __name__ == '__main__':
    unittest.main()
