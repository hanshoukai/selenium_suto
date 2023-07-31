# /usr/bin/env python
# coding=utf-8
from selenium.webdriver.common.by import By
from PO import base_page


# 继承base后既可以调用base的方法也可自己添加新的方法
class SearchPage(base_page.Action):
    # 通过id进行定位元素
    search_loc = (By.ID, "kw")

    def run_case(self, value):
        # 第一种利用原生的send_keys方法
        self.find_element(*self.search_loc).send_keys(value)

        # 第二种利用二次封装的send_keys方法
        # self.send_keys(self.search_loc,value)
