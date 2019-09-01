#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！

#appium 的三种等待
# 1sleep-->强制等待，工作的线程会停止一段时间
# 2隐性等待-->implicitly_wait(time_to_wait)
# 设置最大等待时间，关键字参数：time_to_wait=10，超过最大等待时间后则会抛出异常
#3  安卓独有---->wait_activity()
#  只能用于等待 activity   在设置的时间内没间隔指定的时间扫描activity是否被找到，找到则执行下面的代码，超过最大等待时间则抛出异常
#    activity: 安卓活动名，tiemout：超时时间
# self.dr.wait_activity(activity=".activity.SplashActivity'', timeout=10)
#4 智能等待  智能等待 --- WebDriverWait()：在指定的时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。
# 参数信息： driver：指的是webdriver.Remote()对象 timeout: 最长超时时间，默认以秒为单位 poll_frequency:间隔时间，默认为 0.5 秒 ignored_exceptions - 超时后抛出的异常


# WebDriverWait  等待某一个元素加载出来
# expected_conditions  selenium   的异常处理类
# By  指的是通过什么方式进行定位   例如：   By.ID-->通过ID的方式定位

from selenium   import webdriver
from   selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions   as EC
from  selenium.webdriver.common.by  import By

WebDriverWait('参数1','参数2','参数3').until(EC.presence_of_element_located('参数4'))
"""
参数1：我们与手机建立的会话-->dr
参数2：最大等待时间，单位为s(秒)
参数3：刷新页面的时间间隔，单位s
直到某个元素被找到，停止等待
until(EC.presence_of_element_located('参数4'))
参数4：一个由定位方法，和元素组成的元组   例如：（By.ID,"元素"）
"""