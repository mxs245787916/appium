import pytest
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestDW():
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

    def test_search(self):
        print("搜索测试用例")
        """
        1、打开雪球 app
        2、点击搜索输入框
        3、向搜索框里面输入'阿里巴巴'
        4、在搜索结果里面选择'阿里巴巴'，然后进行点击
        5、获取这只阿里巴巴的股价，并判断这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']").click()
        current_price=float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        print(current_price)
        assert  current_price >200
        time.sleep(5)

    def test_attr(self):
        """
        打开[雪球]应用首页
        定位首页的搜索框
        判断搜索框的是否可用,并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入: alibaba
        判断[阿里巴巴]是否可见
        如果可见，打印"搜索成功”点击，如果不可见，打印"搜索失败”
        """
        element=self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(element.is_enabled())
        search_enabled=element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled ==True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']")
            #判断[阿里巴巴]是否可见
            #alibaba_element.is_displayed()
            print(alibaba_element.get_attribute("displayed"))#返回true
            element_display=alibaba_element.get_attribute("displayed")
            if element_display=='true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
    #滑动操作
        action=TouchAction(self.driver)
        # action.press(x=731,y=2083).wait(10).move_to(x=731,y=484).release().perform()
        #获取屏幕尺寸
        window_rect= self.driver.get_window_rect()
        width=window_rect['width']
        height=window_rect['height']
        x1=int(width/2)
        y_start=int(height *4/5)
        y_end=int(height *1/5)
        time.sleep(5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()
        # time.sleep(5)
        # print('123')

    def test_touchaction1(self):
        print('解锁手势密码')

    def test_get_current(self):
        """
        1、打开雪球 app
        2、点击搜索输入框
        3、向搜索框里面输入'阿里巴巴'
        4、在搜索结果里面选择'阿里巴巴'，然后进行点击
        5、获取这只阿里巴巴香港的股价，通过09988 xpath来定位，并判断这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(current_price)
        assert  current_price>200

    def test_myinfo(self):
        """
        使用uiautomator来进行定位
        1、点击我的，进入到个人信息页面
        2、点击登录，进入到登录页面
        3、输入用户名，输入密码
        4、点击登录
        :return:
        """
        login_account='15158068778'
        login_password='ma15158068778'
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        #my_phone=self.driver.find_element_by_android_uiautomator('new UiSelector().text("请输入手机号或邮箱")')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys(login_account)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys(login_password)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_scroll_find_element(self):
        """
        uiautomator实现滚动查找元素方法使用一下方法滚动查找当前页文本
        ('new UiScrollable(new UiSelector().'
        'scrollable(true).instance(0)).'
        'scrollIntoView(new UiSelector().text("查找的元素文本").'
        'instance(0));')
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("泡沫艺术家").'
                                                        'instance(0));')

if __name__=='__main__':
    pytest.main()
