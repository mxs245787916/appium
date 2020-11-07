import pytest
from appium import webdriver
import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestApi():
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
        self.driver.quit()

    def test_api(self):
        #通过模拟器来打电话/
        self.driver.make_gsm_call('15158068778', GsmCallActions.CALL)
        #发短信
        self.driver.send_sms('15158068778', 'Hey lol')
        #模拟切换网络
        self.driver.set_network_connection(1)

if __name__=='__main__':
    pytest.main()

