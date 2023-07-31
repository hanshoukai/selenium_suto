from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self):
        # 自动识别浏览器版本下载浏览器驱动
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def get_url(self, url):
        # 打开URL
        self.driver.get(url=url)

    def quit_driver(self):
        # 退出driver
        self.driver.quit()

    def send_keys(self, selector, context):
        # 输入文本
        self.driver.find_element(*selector).send_keys(context)

    def click(self, selector):
        # 点击操作
        self.driver.find_element(*selector).click()


