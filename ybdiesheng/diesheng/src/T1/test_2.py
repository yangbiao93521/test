#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！

from   time  import sleep
from selenium   import webdriver
from   selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions   as EC
from  selenium.webdriver.common.by  import By

from   diesheng.until.huadong import *
def   test_1(lian):
    swipe_up(lian )
    WebDriverWait(lian,10,1).until(EC.presence_of_element_located(('By.ID', 'com.tencent.mobileqq:id/ivTitleName')))
    swipe_down(lian)
    WebDriverWait(lian,10,1).until(EC.presence_of_element_located(('By.ID', 'com.tencent.mobileqq:id/ivTitleName')))
    swipe_right(lian )
    WebDriverWait(lian,10,1).until(EC.presence_of_element_located(('By.ID', 'com.tencent.mobileqq:id/settings')))
    swipe_left(lian)
    WebDriverWait(lian,10,1).until(EC.presence_of_element_located(('By.ID', 'com.tencent.mobileqq:id/ivTitleName')))







