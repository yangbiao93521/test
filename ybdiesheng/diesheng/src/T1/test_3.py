#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
from   appium    import webdriver
from    time   import sleep
import yaml
import pytest
from   diesheng.until.ReadDate import s
from selenium.common.exceptions import NoSuchElementException
from    diesheng.until.mylog import get_logger

with open(file=r'E:\ybdiesheng\diesheng\element\login.yaml',mode='r',encoding='utf-8')as  fb:
    g=yaml.load(fb,Loader=yaml.FullLoader)

class  Testtow(object):
    def  test_a(self,lian):
        b=lian
        sleep(2)
        b.find_element_by_xpath(g['xiaoxi']).click()
        sleep(2)
        b.find_element_by_id(g['xiaoxi_xiaoxi']).click()
        sleep(2)
        b.find_element_by_id(g['xiaoxi_guanzhu']).click()
        sleep(2)
        b.find_element_by_id(g['xiaoxi_fensi']).click()
        sleep(2)
        b.find_element_by_id(g['xiaoxi_shengyou']).click()

