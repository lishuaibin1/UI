# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 11:08
# @Author  : Mr.Li

import time


def combobox(driver, content, by_id, by_class, by_ids):     # 下拉框选择定位方法
    driver.find_element_by_id(by_id).click()
    driver.find_element_by_class_name(by_class).send_keys(content)
    time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="select2-ordercreateform-customer_id-results"]/li').click()
    dfds = driver.find_element_by_id(by_ids)     # 整个下拉框的定位
    dsf = dfds.find_elements_by_tag_name('li')      # 下拉框所有内子集的定位
    for dss in dsf:
        if dss.text == content:
            dss.click()
            break       # for循环判断正确选项后要加break停止循环
