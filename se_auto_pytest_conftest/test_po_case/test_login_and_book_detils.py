import pytest
from time import sleep
from page.LoginPage import LoginPage
from page.BookDetilsPage import BookDetilsPage
"""
该文件形成一个完整的流程
在不关闭浏览器，不创建新的driver的前提下，依次执行该py文件下的方法：test01，test02……
"""


def test_01(browser):
    lp = LoginPage(browser)
    lp.get_url("http://novel.hctestedu.com/user/login.html")
    sleep(3)
    lp.do_login("13687300226", "123456")
    sleep(5)


def test_02(browser):
    db = BookDetilsPage(browser)
    db.get_url("http://novel.hctestedu.com/book/150.html")
    db.read_click()
    sleep(5)


def test_03(browser):
    print("1234567890", browser)


# if __name__ == '__main__':
#     pytest.main(["-v", "-s"])
