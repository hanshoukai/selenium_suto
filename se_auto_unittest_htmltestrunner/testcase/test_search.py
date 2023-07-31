# /usr/bin/env python
# coding=utf-8
import unittest
from selenium import webdriver
from PO.search_page import SearchPage
import time


class TestBaiduSearch(unittest.TestCase):
    """UI自动化搜索"""
    def setUp(self):
        self.url = "http://www.baidu.com"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.verificationErrors = []

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_search(self):
        """搜索测试关键字"""
        sp = SearchPage(self.driver)
        sp.open(self.url)
        sp.run_case("测试")
