# /usr/bin/env python
# coding=utf-8

import unittest
from selenium import webdriver
from PO.login_page import LoginPage
import time


class TestBaiduLogin(unittest.TestCase):
    """UI自动化登录"""

    def setUp(self):
        self.url = "http://www.baidu.com"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        # self.verificationErrors = []

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        # self.assertEqual([],self.verificationErrors)

    def test_login(self):
        """百度登录"""
        sp = LoginPage(self.driver)
        sp.open(self.url)
        sp.click_link()
        sp.run_case("hanshoukai", "123321")
        self.assertEqual(sp.get_username(), "hanshoukai", msg="验证失败！")
