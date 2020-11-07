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

    def test_webview(self):
        """
        1、打开雪球应用
        2、点击'交易'
        3、点击'A股开户'
        4、输入用户名和密码
        5、点击'立即开户'
        6、退出应用
        此用例目前存在问题，还未完成
        :return:
        """
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="交易"]').click()
        self.driver.find_element_by_xpath('//*[@content-desc="A股开户"]').click()
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@content-desc="1748a6c1f561e6023fed45a4"]').click()
        # time.sleep(10)
        # self.driver.find_element_by_id('//*[@resource-id="mobile_no"]').sendkey('15158068778')
        # self.driver.find_element_by_id('//*[@resource-id="mobile_code"]').sendkey('123456')

if __name__=='__main__':
    pytest.main()

