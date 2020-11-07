import pytest
from appium import webdriver
import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebdriverwait():
    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "True",
            #中文搜索加2个参数unicodeKeyboard和resetKeyboard
            "unicodeKeyboard": "True",
            "resetKeyboard": "True"
            #"dontStopAppOnReset":"true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        #显式等待 WebDriverWait
        locator=(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']")
        #WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        #lambda
        WebDriverWait(self.driver,10).until(lambda x:x.find_element(*locator))
        self.driver.find_element(*locator).click()
        current_price=float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        print(current_price)
        assert  current_price >200
        time.sleep(5)

if __name__=='__main__':
    pytest.main()
