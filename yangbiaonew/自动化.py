#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
from   appium    import webdriver
from    time   import sleep
# python代码客户端连接手机时需要的信息
d={
  "platformName": "Android",            #设备的系统类型
  "platformVersion": "8.1.0",           #手机系统版本
  "deviceName": "cf8eca98",              #手机序列号
  "appPackage": "com.tencent.mobileqq",  #APP的包名
  "appActivity": ".activity.SplashActivity",   #活动名称
  "noReset": "true"                                #是否重置应用程序状态
}
# 步骤1：与手机建立连接    localhost=127.0.0.1       将手机信息发送到appium 服务器，使服务器和手机建立一个seeion
# appium与python客户端建立一个连接
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
sleep(5)
"""
1.python与appium服务器建立一个连接
2.python中的命令由appium服务器转发
3.手机中的bootstrap.jar服务器接收转发的命令
4.处理转发命令，将命令下发给uiautomator(手机自带的测试框架：执行类似于adb命令)
5.uiautomator生成一个执行之后的结果
6.结果转发给bootstrap.jar微服务器
7.一直转发到python客户，appium库解析结果
8.将结果输出出来
"""
"""
id:一般是唯一的，是标记一个元素
class：标记一组元素，一般是多个
text：是否可以获取文字，有文字代表可以获取，没有代表不可以
clickable：判断是否可以被点击，true代表可以被点击，false代表不可以
"""
# 执行操作
"""                                                   
id不唯一，使用class定位
解决方法：向上一级或者上上一级查找ID唯一、class唯一
        再使用class进行定位
"""
#先找唯一的ID,再找class
#联系人、看点、动态、三个组成的列表[1,2,3]
s=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.TextView')
for    i   in s:
    print(i.text)
    sleep(2)
# dr.find_element_by_id('android:id/tabs').find_element_by_class_name('android.widget.RelativeLayout').find_element_by_class_name('android.widget.TextView')

# dr.find_element_by_id('com.tencent.mobileqq:id/relativeItem').click()
# sleep(3)
# dr.find_element_by_class_name('android.widget.EditText').send_keys('hello')
# sleep(3)
# dr.find_element_by_class_name('android.widget.Button').click()


