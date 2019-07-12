# -*- coding: utf-8 -*-
# @Time    : 2019/6/22 14:05
# @Author  : Mr.Li

import unittest
import os
import HTMLTestRunner
import datetime

def allTests():
    """获取所有用例"""
    suite = unittest.TestLoader().discover(
        start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'TestCase'),
        pattern='test_*.py',
        top_level_dir=None)
    return suite

def getNowTime():
    """获取现在时间"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')

def run():
    """运行测试用例并生成测试报告"""
    gh = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report', getNowTime()+' '+'testReport.html')
    HTMLTestRunner.HTMLTestRunner(
        stream=open(gh, 'wb'),
        verbosity=2,
        title='优装汇测试报告',
        description='优装汇测试报告详细信息').run(allTests())

if __name__ == '__main__':
    run()

