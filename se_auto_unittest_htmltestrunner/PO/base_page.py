# /usr/bin/env python
# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

'''
这个类主要是完成所有页面的一些公共方法的封装
'''


class Action(object):
    # 初始化
    def __init__(self, se_driver):
        self.driver = se_driver

    # 定义open方法
    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # 重写元素定位的方法
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print("未找到%s" % (self, loc))

    # 定义script方法，用于执行js脚本
    def script(self, src):
        self.driver.execute_script(src)

    # 重写send_keys方法
    def send_keys(self, loc, value, clear_first=True, clik_first=True):
        try:
            if clik_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("未找到%s" % (self, loc))
