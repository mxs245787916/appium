import time

from appium import webdriver

desire_cap={
   "platformName": "Android",
   "deviceName": "emulator-5554",
   "appPackage": "com.xueqiu.android",
   "appActivity": ".view.WelcomeActivityAlias",
   "noReset": "True"
   #"dontStopAppOnReset":"true"
}

driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)

#增加隐士等待
driver.implicitly_wait(10)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.back()
#driver.back()
driver.quit()