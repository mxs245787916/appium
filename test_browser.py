import pytest
from appium import webdriver
import time

from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

####webview测试
class TestBrowser():
    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "browserName": "Browser",
            "noReset": "True",
            "deviceName": "emulator-5554"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id('index-kw').click()
        self.driver.find_element_by_id('index-kw').send_keys('appium')
        #增加显式等待
        search_loctor=(By.ID,'index-bn')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(search_loctor))
        self.driver.find_element(*search_loctor).click()


# if __name__=='__main__':
#     pytest.main()
