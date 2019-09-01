#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
"""
pytest是python自动化测试的一个工具库
作用：
1.调整测试用例的运行顺序
2对测试用例传入测试数据
3对测试用例设置断言
pytest与allure生成测试报告
特点：
灵活、支持的插件丰富
"""
import pytest
"""
自动化测试用例指的是？
    指的是一个函数，必须以test开头
"""
import pytest
def      test_0():
    n=0
    for  i  in  range(1,101):
        n+=i
        # 预期结果是5050
        # 实际结果是n
        # 断言：那拿实际结果与预期结果进行对比的过程
    assert  n==5051
# 执行测试用例
"""
1.pytest
2.py.test
"""
# https://www.cnblogs.com/Detector/p/9302428.html

# 1、py.test test_1.py --alluredir ./result/      执行测试用例将数据保存在result目录中
# 2、allure generate ./result/ -o ./report/ --clean   生成测试用例html报告
# 3、allure open -h 127.0.0.1 -p 8083 ./report/         打开生成的HTML测试报告


"""
pytest:
查找当前目录下，所有文件或目录，找包含test目录和文件，
如果找到test开头的目录，类似于cd，执行所有test开头的文件；
搜索test开头所有的函数

整个当前目录下没有包含test的文件和目录：
抛出：_____ERROR collecting test session ____


pytest
-v    使输出信息更加详细
-q    简化输出信息0
-k    执行包含设定"关键字"的用例
-s    输出测试用例中包含print的信息
pytest  脚本名：:用例名字-->运行执行脚本中的具体用例
"""

