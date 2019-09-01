#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
import pytest
from   appium  import webdriver
from    time   import sleep
@pytest.fixture(scope='module')
def lian():
    d = {
        "platformName": "Android",
        "platformVersion": "8.1.0",
        "deviceName": "cf8eca98",
        "appPackage": "com.tencent.mobileqq",
        "appActivity": ".activity.SplashActivity",
        "noReset": "true"
    }
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
    sleep(1)
    print('ok')
    return dr
