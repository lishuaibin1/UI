# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 17:15
# @Author  : Mr.Li

from page.dingdan import *
import json

class read(OrderManagement):

    def read_file1(self):
        json_path = self.path(filename='dingdanliebiao.json')
        with open(json_path, encoding="utf-8") as f:
            wqr = json.load(f)['NewOrder']
        return wqr

    def read_file2(self, dataClass):
        json_path = self.path(filename='dingdanliebiao.json')
        with open(json_path, encoding="utf-8") as f:
            wqr = json.load(f)['dingdanguanliyemian'][dataClass]
        return wqr

    def read_file3(self, data):
        json_path = self.path(filename='dingdanliebiao.json')
        with open(json_path, encoding="utf-8") as f:
            wqr = json.load(f)[data]
        return wqr
