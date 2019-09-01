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

class  Testone(object):
    def    test_a(self,lian):
        sleep(3)
        a=lian
        c=a.find_elements_by_id(g['sigekuang'])
        for  i  in   c:
            sleep(3)
            i.click()
            a.find_element_by_id(g['xiaochuangkou']).click()
            sleep(3)
            a.find_element_by_id(g['tuichufangjian']).click()











