from selenium.webdriver.common.by import By
from base.BasePage import BasePage
from time import sleep


class BookDetilsPage(BasePage):
    # 页面上的元素
    hc_readbtn = (By.CSS_SELECTOR, ".bookChapter>.book_tit>.fr")

    # 页面上的操作
    def read_click(self):
        self.click(self.hc_readbtn)
