import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = None


@pytest.fixture(scope="session")
def browser():
    global driver
    if driver is None:
        # 单个执行模式
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.maximize_window()
    # yield 用于去执行测试逻辑中写的代码
    yield driver
    # driver退出
    driver.quit()


