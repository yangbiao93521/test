#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
from   appium    import webdriver
from    time   import sleep
import yaml
import pytest
from   QQ.until.ReadDate import s
from selenium.common.exceptions import NoSuchElementException
from    QQ.until.mylog import get_logger
v=get_logger(filename='test_1.py')


with open(file=r'E:\ybtest\QQ\element\login.yaml',mode='r',encoding='utf-8')as  fb:
    e=yaml.load(fb,Loader=yaml.FullLoader)
print(e)

# class   Testone(object):

#     # def lian(self):
#     #     d={
#     #         "platformName": "Android",
#     #         "platformVersion": "8.1.0",
#     #         "deviceName": "cf8eca98",
#     #         "appPackage": "com.tencent.mobileqq",
#     #         "appActivity": ".activity.SplashActivity",
#     #         "noReset": "true"
#     #     }
#     #     dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
#     #     return dr
#     def  test_a(self,lian):
#         sleep(1)
#         a=lian
#         a.find_element_by_xpath(e['tou']).click()
#         sleep(1)
#         a.find_element_by_id(e['seting']).click()
#         sleep(1)
#         a.find_element_by_id(e['zhanghao']).click()
#         sleep(1)
#         a.find_element_by_id(e['tuihao']).click()
#         sleep(1)
#         a.find_element_by_id(e['tuichu']).click()
#         sleep(1)
#         assert a.find_element_by_accessibility_id(e['xinyonghu']).text=='用户注册'
#     def  test_b(self,lian):
#         sleep(1)
#         b=lian
#         b.find_element_by_accessibility_id(e['shurukuang']).clear()
#         sleep(1)
#         b.find_element_by_accessibility_id(e['shurukuang']).send_keys('1654401689')
#         sleep(1)
#         b.find_element_by_id(e['mima']).clear()
#         sleep(1)
#         b.find_element_by_id(e['mima']).send_keys('wyyzxml93521')
#         sleep(1)
#         b.find_element_by_id(e['denglu']).click()
#         sleep(1)
@pytest.mark.parametrize('y1,y2',s)
def  test_c(lian,y1,y2):
                sleep(1)
                f=lian
                f.find_element_by_accessibility_id(e['shurukuang']).clear()
                sleep(1)
                f.find_element_by_accessibility_id(e['shurukuang']).send_keys(y1)
                sleep(1)
                f.find_element_by_id(e['mima']).clear()
                sleep(1)
                f.find_element_by_id(e['mima']).send_keys(y2)
                v.info(f'账号是{y1},密码是{y2}')
                sleep(1)
                f.find_element_by_id(e['denglu']).click()
                sleep(5)




