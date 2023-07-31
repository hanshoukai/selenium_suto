# /usr/bin/env python
# coding=utf-8
from selenium.webdriver.common.by import By
from PO import base_page
import time


class LoginPage(base_page.Action):
    link_loc = (By.LINK_TEXT, "登录")
    name_loc = (By.ID, "TANGRAM__PSP_8__userName")
    password_loc = (By.ID, "TANGRAM__PSP_8__password")
    submit_loc = (By.ID, "TANGRAM__PSP_8__submit")

    username_top = (By.LINK_TEXT, "hanskai")

    def click_link(self):
        self.find_element(*self.link_loc).click()
        time.sleep(3)  # 等待3秒，等待登录弹窗加载完成

    def run_case(self, value1, value2):
        self.find_element(*self.name_loc).send_keys(value1)
        self.find_element(*self.password_loc).send_keys(value2)
        time.sleep(20)  # 手动输入验证码
        self.find_element(*self.submit_loc).click()
        time.sleep(5)  # 等待5秒，登录后的页面加载完成

    def get_username(self):
        return self.find_element(*self.username_top).text
