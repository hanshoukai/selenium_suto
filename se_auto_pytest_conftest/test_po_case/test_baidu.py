import pytest
from time import sleep
from page.BaiduPage import BaiduPage


def test_01(browser):
    lp = BaiduPage(browser)
    lp.get_url("http://www.baidu.com")
    sleep(3)
    lp.do_search("测试")
    sleep(5)

