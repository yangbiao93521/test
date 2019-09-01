#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
"""
清理测试环境的一个机制
第一步：在用执行用例之前进行环境清理
第二步：在用例之后进行环境清理
"""
# 脚本级别的清理
# setup_module用例执行之前的
# teardown_module用例执行之后的
# module 本脚本所有的用例执行前、执行后的操作仅执行一次
import pytest
# def   setup_module():
#     print("所有用例执行之前执行一次")
# def    test_1():
#     print('用例1执行')
# def   test_2():
#     print('用例2执行')
# def   test_3():
#     print('用例3执行')
# def   teardown_module():
#     print('每个用例执行之后执行一次')

# setup_function   每个测试用例执行之前都要执行一次
# teardown_module    每个测试用例执行之后都要执行一次
# def   setup_function():
#     print("每个用例执行之前执行一次")
# def    test_1():
#     print('用例1执行')
# def   test_2():
#     print('用例2执行')
# def   test_3():
#     print('用例3执行')
# def   teardown_function():
#     print('每个用例执行之后执行一次')

# setup   teardown    在类的范围内使用
# class     Testone(object):
#     def  setup(self):
#         print('执行setup')
#     def   teardown(self):
#         print('执行teardown')
#     def   test_4(self):
#         print('执行用例4')
#     def  test_5(self):
#         print('执行用例5')
#     def   test_6(self):
#         print('执行用例6')

#setup-->每个测试用例之前运行一次
# teardown-->每个测试用例执行之后运行一次

# setup_class  -->类中的所有测试用例之前执行一次
# teardown_class -->类中的所有测试用例执行之后执行一次

# class     Testtow(object):
#     def  setup_class(self):
#         print('执行setup')
#     def   teardown_class(self):
#         print('执行teardown')
#     def   test_4(self):
#         print('执行用例4')
#     def  test_5(self):
#         print('执行用例5')
#     def   test_6(self):
#         print('执行用例6')

# setup_method -->方法级别的
# teardown_method-->
# class     Testthree(object):
#     def  setup_method(self):
#         print('执行setup_method')
#     def   teardown_method(self):
#         print('执行teardown_method')
#     def   test_4(self):
#         print('执行用例4')
#     def  test_5(self):
#         print('执行用例5')
#     def   test_6(self):
#         print('执行用例6')
# setup_method   每个测试用例执行之前执行一次
# teardown_method    每个测试用例执行之后执行一次

# 测试夹具fixture
# @pytest.fixture()
""""
scope:装饰器的作用范围
    function   方法级别、默认
    class      类级别的
    module     脚本级别的,在测试用例执行之前运行一次，仅运行一次
               使用方式：在测试用例的（放入被@pytest.fixture装饰的函数名）
    package    目录级别的
    session    会话级别的，多个测试用例组合的时候用
    conftest.py:存放公共函数
                test开头的脚本，一般只写test开头的类、方法、函数
                注意事项：conftest.py必须放在当前测试用例所在的目录下面
"""

# import pytest
# @pytest.fixture()
# def   login():
#     print('login函数开始执行')
# def    test_1(login):
#     print('执行用例1')
# def test_2(login):
#         print('执行用例2')
# def    test_3(login):
#     print('执行用例3')
# def    test_4():
#     print('执行用例4')


# class   Test(object):
#     @pytest.fixture(scope='class')
#     def  login(self):
#         print('执行login')
#     def   test_1(self,login):
#         print('执行用例1')
#     def   test_2(self,login):
#         print('执行用例2')
#     def  test_3(self,login):
#         print('执行用例3')
#     def   test_4(self):
#         print('执行用例4')




# import pytest
# @pytest.fixture(scope='module')
# def    start():
#     print('所有测试用例执行一次之前')
# @pytest.fixture(scope='module')
# def close():
#     print('所有测试用例执行一次之前')
# def   test_1(start):
#         print('执行用例1')
# def   test_2(start):
#         print('执行用例2')
# def  test_3(start):
#         print('执行用例3')
# def   test_4(close):
#         print('执行用例4')


#conftest.py
"""
conftest.py:python文件，用来存放公共函数
"""

# def   test_1():
#     print('输入账号密码')
# def  test_2(clean):
#     print('输入账号密码')
# def    test_3():
#     print('输入账号密码')



# 参数化-->向测试用例中传入参数的过程
d=[1,2,3,4,5,6,7]
@pytest.fixture(scope='function',params=d)
def   read_data(request):
    #request：固定写法
    #作用：取出参数列表中的每一个元素
    #request.param:固定写法
    #作用:与request结合使用，取出参数
    print(f'当前的参数是传入的参数值是{request.param}')
    return request.param
def   test_1(read_data):
    t=read_data    #实际结果
    assert  t<6

#传入两个参数
# d2=[(1,2,3),(2,2,2),(3,4,3)]
# @pytest.mark.parametrize('y1,y2',d2)
# def   test_2(y1,y2):
#     print(f'y1的值是{y1}')
#     print(f'y2的值是{y2}')
#     assert y1==y2
# @pytest.mark.parametrize('y1,y2,y3',d2)
# def  test_3(y1,y2,y3):
#     assert y1==y2==y3
#
# @pytest.fixture(autouse=True)
# def myfix():
#     print('每个测试都要跑myfix')
# # @pytest.mark.usefixtures('myfix')
# # pytestmark=pytest.mark.usefixtures("myfix")
# #
# def   test_1():
#             print('执行用例1')
# def   test_2():
#             print('执行用例2')
# def  test_3():
#             print('执行用例3')
# def   test_4():
#             print('执行用例4')

#ids:
#name:
#pytest跳过某些用例、失败重跑、统计测试覆盖率、等





