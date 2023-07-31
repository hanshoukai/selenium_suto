from selenium.webdriver.common.by import By
from base.BasePage import BasePage
from time import sleep


class BaiduPage(BasePage):
    # 1、定义页面全部元素
    search_loc = (By.ID, "kw")
    click_loc = (By.ID, "su")

    # 2、页面的操作，一个函数封装为一个操作
    def do_search(self, value):
        self.click(self.search_loc)
        self.send_keys(self.search_loc, value)
        self.click(self.click_loc)
