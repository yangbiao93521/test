#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
from   selenium   import webdriver
from  time   import   sleep
import os
import selenium.webdriver.support.ui as ui
from  selenium.webdriver.common.action_chains import ActionChains
import pytest




#访问网址
dr=webdriver.Chrome()
sleep(2)
dr.get('https://mail.163.com/')
# dr.switch_to.frame('login_frame')
#获取访网址的标题
# a=dr.title
# # print(a)
# # #获取访问的网址
# # dr.set_window_size(1000,1000)
# # #设置浏览器打开的位置
# # dr.set_window_position(600,800)
# # #最大化浏览器
# # dr.maximize_window()
# # #最小化浏览器
# # dr.minimize_window()
# dr.get('https://www.baidu.com')
# sleep(2)
# dr.get('https://www.jd.com')
#回退到上一次的页面
# dr.back()
#前进到第二个页面
# dr.forward()

"""
核心：定位
1.ID   2.class_name   3.name  4.link  text   5.tag_name    6.XPATH   7.css    8.  partial_link_text 
定位准确度：ID 、xpath 、name 、css  
"""

#1.ID定位     动作：1.clcik() 2.send_keys('内容')
# dr.find_element_by_id('kw').send_keys('python').find_elements_by_id('su').click()
#2.class定位    唯一的
# dr.find_elements_by_class_name('')
#3.name   指的就是name 属性
# dr.find_elements_by_name('')
#4.link  test   文本定位
# dr.find_element_by_link_text('新闻').click()
#5.partial_link_text    模糊文本
# dr.find_element_by_partial_link_text('新').click()
# 6.tag_name   标签定位   通常定位一组元素
# dr.find_element_by_tag_name('')
#7.xpath 路径标记语言    绝对路径和相对路径    xml：可扩展标记语言，内容跟HTML一样的，用来储存数据的
#    一个/是绝对路径，两个//是相对路径
# dr.find_elements_by_xpath('//*[@id="u1"]/a[1]')
#8.css   层叠样式表
# dr.find_elements_by_css_selector('#u1 > a:nth-child(1)')
# dr.find_element_by_id('u').send_keys('1654401689')
# dr.find_element_by_id('p').send_keys('wyyzxml93521')
# dr.find_element_by_class_name('btn').click()
# sleep(3)
# dr.find_element_by_xpath('//*[@id="composebtn"]').click()

#同时定位多个元素,结果是个列表
#层级定位：先定位一个大的范围，在从大的范围重定位元素
#dr.父元素.子元素.动作
#父元素必须是唯一的
#子元素可以是一组，可以是唯一的

#iframe:内嵌框架
#切换框架   只可以用ID或name的值来定位
#没有ID，没有name，先定位到框架，在切换
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# dr.find_element_by_id('u').send_keys('1654401689')
# dr.find_element_by_id('p').send_keys('wyyzxml93521')
# sleep(2)
# dr.find_element_by_id('login_button').click()

#退出到第一层页面
# dr.switch_to.default_content()
#退出到上一层框架
# dr.switch_to .parent_frame()

#浏览器管理窗口的原理：
#浏览器会对每个打开的窗口生成一个唯一标识窗口的句柄
#谷歌产生的句柄是一堆字符串
#火狐产生的是一堆数字

#获取当前窗口的句柄
# dd=dr.current_window_handle
# print(dd)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# sleep(2)
# #获取所有窗口的句柄
# dd=dr.window_handles
# print(dd)
# #切换窗口
# dr.switch_to.window(dd[-1])
#
# a=dr.title
# print(a)

# dr.find_element_by_xpath('/html/body/button').click()
# sleep(2)
# #处理弹出框   alert弹出框
# #将控制器切换到弹出框
# ww=dr.switch_to.alert
# print(ww.text)   #获取弹出框上的文本
#
# ww.send_keys('我问问你')
# ww.accept()  #点击弹出框上的确定
# # ww.dismiss()   #点击弹出框上的取消

#执行JavaScript函数
#1.滚动条滚动到指定位置
# dd=dr.find_element_by_xpath('//*[@id="tabs"]/div[1]/div[2]/a')
# sleep(2)
# dr.execute_script('arguments[0].scrollIntoView();',dd)

#2更改页面的高度滑动滚动条   10000指的是高度
# for i in range(0,10000,200):
#     js=f'var q=document.documentElement.scrollTop={i}'
#     dr.execute_script(js)
#     sleep(2)

#QQ邮箱发邮件
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# dr.find_element_by_id('u').send_keys('1654401689')
# dr.find_element_by_id('p').send_keys('wyyzxml93521')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="composebtn"]').click()
# # dr.find_element_by_id('mainFrameContainer')
# dr.switch_to.frame('mainFrame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('cc524997199@163.com')
# dr.find_element_by_xpath('//*[@id="subject"]').send_keys('一稿我力高')
# sleep(3)
# dr.switch_to.frame(dr.find_element_by_class_name('qmEditorIfrmEditArea'))
# dr.find_element_by_xpath('/html/body').send_keys('嘴角向上，拥抱太阳')
# dr.switch_to .parent_frame()
# dr.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()

#163邮件发送
dr.find_element_by_xpath('//*[@id="switchAccountLogin"]').click()
sleep(2)
dr.switch_to.frame(dr.find_element_by_xpath('//*[@id="loginDiv"]/iframe'))
dr.find_element_by_xpath('//*[@id="account-box"]/div[2]/input').send_keys('18783828252')
dr.find_element_by_name('password').send_keys('935210')
dr.find_element_by_id('dologin').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="_mail_component_24_24"]').click()
sleep(2)
dr.find_element_by_class_name('nui-editableAddr-ipt').send_keys('734351303@qq.com')
dr.find_element_by_xpath('//*[@id="_mail_input_3_201"]/input').send_keys('极致骚男')
dr.switch_to.frame(dr.find_element_by_xpath('//*[@id="_mail_editor_0_205"]/div[1]/div[2]/iframe'))
dr.find_element_by_xpath('/html/body').send_keys('风扇开三挡')
dr.switch_to.parent_frame()
dr.find_element_by_xpath('//*[@id="_mail_button_8_206"]/span[2]').click()








#等待
#强制等待：sleep()
#智能等待
# until=ui.WebDriverWait(dr,100)
# #定位要出现的元素
# until.until(lambda dr:dr.find_element_by_xpath('//*[@id="J_footer"]/div[1]/div/ul/li[1]/div/p').is_displayed())

# ww=dr.find_elements_by_class_name('cate_menu_item')
# for  i  in  ww:
# #     动作链：动作链控制鼠标移动到某个元素的中心点
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)

#拖拽
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('988738983')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('dasde3462198r')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# dd=dr.find_element_by_xpath('//*[@id="tcaptcha_iframe"]')
# dr.switch_to.frame(dd)
# sleep(2)
# ww=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
# ActionChains(dr).drag_and_drop_by_offset(ww,180,0).perform()
# ActionChains(dr).drag_and_drop('起始','终点')
