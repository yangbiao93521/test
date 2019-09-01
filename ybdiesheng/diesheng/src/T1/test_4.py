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
class   Testthree(object):
    def  test_a(self,lian):
        a=lian
        sleep(2)
        a.find_element_by_xpath(g['paihang']).click()
        sleep(2)
        a.find_element_by_id(g['meilibang']).click()
        sleep(2)
        a.find_element_by_id(g['meilibang_ribang']).click()
        sleep(2)
        a.find_element_by_id(g['meilibang_zhoubang']).click()
        sleep(2)
        a.find_element_by_id(g['meilibang_yuebang']).click()
        sleep(2)
        a.find_element_by_id(g['caifubang']).click()
        sleep(2)
        a.find_element_by_id(g['caifubang_ribang']).click()
        sleep(2)
        a.find_element_by_id(g['caifubang_zhoubang']).click()
        sleep(2)
        a.find_element_by_id(g['caifubang_yuebang']).click()
        sleep(2)
        a.find_element_by_id(g['liwu']).click()
        sleep(2)
        a.find_element_by_id(g['liwu_ribang']).click()
        sleep(2)
        a.find_element_by_id(g['liwu_zhoubang']).click()
        sleep(2)
        a.find_element_by_id(g['liwu_yuebang']).click()
        sleep(2)







