#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
# python装饰器
#作用:将函数作为参数进行返回给别的函数使用
def     foo(a):
    print('执行foo函数开始')
    a()
    print('执行foo函数结束')

def   koo():
    print('执行了koo函数')
foo(koo)

# 函数的执行规则：函数名+（）
def    out(a):
    print('开始执行out函数')
    def  inner():
        a()
    print('执行out函数结束')
    return inner
# @python的语法糖  @out 使用out这个装饰器
@out
def  say_hello():
    print('hello,装饰器')
say_hello()

out(say_hello)()