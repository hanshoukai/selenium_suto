import pytest
from time import sleep
from page.LoginPage import LoginPage
from page.BookDetilsPage import BookDetilsPage


def test_01():
    lp = LoginPage()
    lp.get_url("http://novel.hctestedu.com/user/login.html")
    sleep(3)
    lp.do_login("13687300226", "123456")
    sleep(5)
    lp.quit_driver()


def test_02():
    db = BookDetilsPage()
    db.get_url("http://novel.hctestedu.com/book/150.html")
    db.read_click()
    sleep(5)


if __name__ == '__main__':
    pytest.main(["-v", "-s"])
