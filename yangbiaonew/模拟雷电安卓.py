#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
from   appium    import webdriver
from    time   import sleep
d={
  "platformName": "Android",            #设备的系统类型
  "platformVersion": "5.1.1",           #手机系统版本
  "deviceName": "emulator-5554",              #手机序列号
  "appPackage": "com.tencent.mobileqq",  #APP的包名
  "appActivity": ".activity.SplashActivity",   #活动名称
  "noReset": "true"                                #是否重置应用程序状态
}
dr=webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)