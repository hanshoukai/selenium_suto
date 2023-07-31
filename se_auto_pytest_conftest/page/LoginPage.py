from selenium.webdriver.common.by import By
from base.BasePage import BasePage


class LoginPage(BasePage):
    # 1、定义页面全部元素
    hc_username = (By.XPATH, "//input[@id='txtUName']")
    hc_password = (By.XPATH, "//input[@id='txtPassword']")
    hc_loginbtn = (By.XPATH, "//input[@id='btnLogin']")
    hc_quit = (By.XPATH, "//*[@id='headerUserInfo']/span/a[2]")

    # 2、页面的操作，一个函数封装为一个操作
    def do_login(self, username, password):
        self.send_keys(self.hc_username, username)
        self.send_keys(self.hc_password, password)
        self.click(self.hc_loginbtn)

    def quit_login(self):
        self.click(self.hc_quit)


