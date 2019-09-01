#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
#https://testerhome.com/topics/15649   详解
import allure
import pytest

#feature: 标注测试用例是哪一个模块的
@allure.feature('模块一')
def    test_1():
    assert 0==0

@allure.feature('模块一')
def test_2():
    assert 0 == 0

#story:对一个测试用例的详细描述
@allure.feature('模块二')
@allure.story('这是一个牛逼的测试用例')
def   test_3():
    assert 0>1234567
@allure.feature('模块二')
@allure.story('这是一个垃圾的测试用例')
def   test_4():
    """
    这是对函数参数、返回值的一个注释、讲解
    自我感觉老厉害了
    """
    #测试用例的描述是通过函数的注释来获取到的
    assert '香港是中国的'

#测试用例的优先级
"""
Blocker级别：阻塞中断缺陷
Critical:临界缺陷   严重缺陷
Normal级别：普通缺陷
Minor级别：次要
Trivial级别：轻微
"""

#severity--标注而是用例的优先级的

@allure.feature('模块三')
@allure.severity('blcoker')
def   test_5():
    assert 0<1234
@allure.feature('模块三')
@allure.severity('critical')
def   test_6():
    assert 0<1234
@allure.feature('模块三')
@allure.severity('normal')
def   test_7():
    assert 0<1234
@allure.feature('模块三')
@allure.severity('minor')
def   test_8():
    assert 0<1234
@allure.feature('模块三')
@allure.severity('trivial')
def   test_9():
    assert 0<1234

#setp    记录测试中的一些步骤，日志代码可以通过setp记录到报告中
@allure.feature('模块四')
@allure.step('字符串相加：{0}，{1}')
#isinstance(参数一，参二)，判断数据类型的类，参数一和参数二是否是同一个
def  str_add(str1,str2):
    if  not   isinstance(str1,str):
        return f'{str1}不是字符串类型的'
    if  not   isinstance(str2,str):
        return f'{str2}不是字符窜类型的'
    return str1+str2

@allure.feature('模块五')
def   test_10():
    str1='hello'
    str2='world'
    assert str_add(str1,str2)=='helloworld'

#issue 和testcase
#对issue  和 testcase  生成一个网址
@allure.feature('模块六')
@allure.issue("http://www.baidu.com")
@allure.testcase("http://www.testlink.com")
def test_case():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'


file = open('E:\ybtest\QQ\src\T2\result\123.png', 'rb').read()
allure.attach('123.png', file, allure.attachment_type.png)