# -*- coding: utf-8 -*-
# python——>函数
"""
函数的作用？
1.使代码重复被使用
2.减少代码量
"""
# 函数的定义？
# 一段代码的封装被称为函数
# 函数的书写格式？
"""
1.定义函数的关键字  def
2.函数名：要符合变量的命名规则
3.参数：分为关键字参数(必填参数）、默认参数、可变长参数
4.返回值：使用关键字  return
"""
# def  add(a):
#     # 求和的代码
#     b=0
#     for i  in  range(a):
#         b+=i
#     print(b)
#     # return b
#     # return   #没有返回结果  返回None（空）
# add(101)
# print(sum(range(101)))
"""
1.一个函数使用return，但是没有返回的结果时，返回None（空）
2.一个函数不使用return时，返回None（空）
"""



# 如何使用函数？
"""
1.函数的名字
2.有参数对单数赋值
"""
# print（add（201））

# 全局变量、局部变量、函数的作用域、函数的变量
# 全局变量
# a="全局变量"
# """
# 全局变量：定义之后整个脚本都可以使用
# """
# print(a)
#
# # 局部变量
# """
# 定义之后只能在指定的范围内使用
# """

# def  pp():
#     b="局部变量"
#     return  b
# pp()   # 等价于”局部变量"
# print(pp())
#

# global
#将局部变量转为全局变量
#修改全局变量的数据类型
# """
# 作用：将局部变量转变成全局变量
# """
# def   k():
#     global  p  #p代表全局变量
#     p=100
# k()
# print(p)

# 当全局变量和局部变量是同一个变量名的时候，函数优先使用局部变量
# 当函数内没有局部变量时，向上查找相同名字的全局变量，找不到需要的全局变量时，代码报错
# 修改全局变量的数据类型
# g="全局变量"
# def  k():
#     global g   #全局变量
#     g=100
#     print(g)
# k()
# print(g)

#pycharm 调试  debug
"""
红点：被称为调试模式
进入调试模式：绿色的小虫子
"""
# def  k(x1,x2):
#     c=x1+x2
#     print(c)
#     return c
# k(100,200)

"""
函数的作用域？
从定义函数的那一行开始，一直到return那一行结束
"""

#接阶乘之和的函数
# def  jiecheng(x):
#     m=1
#     n=0
#     for a in range(1,x+1):
#        m=m*a
#        n=n+m
#     print(n)
#     return n
# print(jiecheng(5))
#
# 函数的参数分类？
#1.必填参数：参数定义之后，在函数被使用的时候，必须传入，赋值的参数
#2.默认参数：在参数被定义的时候，参数有一个默认值，在函数被使用的时候对默认参数赋值，则使用赋予值，不对默认参数赋值，则使用默认值
# 例如：
# def  k(x1,x2=5000):
#     c=x1+x2
#     print(c)
#     return c
# k(100,199)
# k(100)

# 可变长参数
# """
# 1.以元组的形式赋值
# """
# def d(*args):
#     print(args)
# d(1,2,3,4,5,6)



#     for i in range(0,e):
#         a=f"s_{i}"
#         print(f"参数值是{a}，对应值是{cc[i]}")
# d(1,2,3)


# 2.以字典的形式赋值
# def  k(**kwargs):
#     print(kwargs)   #kwargs字典，关于字典的所有的函数都可以用
# # 参数传递,写法1
# k(a=1,b=2,c=3)
#
# # 写法2,先写成一个字典，**变量名
# n={"a":1,"b":2,"c":3}
# k(**n)


# 冒泡函数
# def   a(*x):
#     c=list(x)
#     d=len(c)
#     for  i   in  range(d):
#             for  j   in  range(d-1):
#                 if  int(c[j])>int(c[j+1]):
#                     c[j],c[j+1]=c[j+1],c[j]
#     return c
# print(a(-1,3,5,23,32323))


# def a(x,y):
#     b=x.split(",")
#     c=y.split(",")
#     d=[]
#     e=[]
#     for  i  in  range(len(b)):
#         if     len(b[i])>=5   and  len(b[i])<=8:
#             for j in range(len(c)):
#                 if   len(c[j])>=6   and  len(c[j])<=9:
#                     d.append(d[i])
#                     e.append(e[j])
#     print(d)
#     print(e)
# a("dsadsad,sadsadsa,dsadsadsadsa,dsadsadsadsadsa,dsadadsa,sadsadsadsa,sadasdsaadsad,eqwrdqwfdsacd,sadsadsad,sadsa","dadsajdoisahdoihc,dsadsad,sadsaddsad,daa,sadsadsadsadsadsa,asdad")


# 函数的嵌套
# 格式1
# def   foo():
#     """
#     函数语句块
#     """
#     return  "我是foo函数的第一段话"
# def  k():
#     print("此时运行函数k")
#     print(foo())   #执行foo函数
# k()

# 格式2
# def  foo():
#     x=100   #局部变量
#     def  k():
#         c=x*10
#         return c
#     return k()
# print(foo())


# 匿名函数？
"""
1.函数没有名字
2.使用lambda定义
3.作用和函数的作用相同
"""
# 定义匿名函数的格式
"""
lambda  参数1，参数2，。。。
"""
#
# import random
# a=lambda n : random.randint(1,10)*n
# print(a(3))

# python的列表推导式
# 定义：
"""
1.生成的结果是列表
2.可以使用循环语句、if语句
3.使用python的库（模块）
4.
"""
# 列表推导式的书写格式
"""
[表达式 循环语句  判断]
"""

# b=[i+1 for i  in  range(1,11) if  i > 5]
# b.reverse()
# print(b)
# print(b[::-1])

# b=[ lambda i : i+1  for    i  in  range(10)  ]
# print(b[0](3))

# a=[[1,2],[2,3],[3,4]]
# b=[  a[len(a)]  for  i   in   range(len(a))            ]
# print(b)



# open():打开文件  .txt    excle文件
# 如何查看文件
# 常用参数
# 1.file：     文件的名字，a.txt   b.excel
# 2.mode='r'     读取文件的模式    r——读取模式    w——写入模式     a——追加写入模式
# #                               b——二进制写入   + 追加  读写
# 3。encoding=None      指定文件的编码方式       utf - 8     gbk

# """
# 1.选中
# 2.ctrl  +   b
# """
#向文件中写入内容
# f=open("a.txt",mode="w",encoding="utf-8")
# # wrrite():写入  传入字符串，想写入的文字
# f.write("hello python")
# f.close()  #关闭


# 读取文件中的内容
# f=open(file="a.txt",encoding="utf-8")
# # # read（）：读取文件中所有的内容
# text=f.readlines(2)
# # readlines（）：每次读取一行，n有数值，读取指定数值的行数，返回一个列表
# print(text)
# f.close()


# a=["a","b","c"]
# # f=open(file="a.txt",mode="w",encoding="utf-8")
# # for   i   in    a:
# #     f.write(i+"\n")
# #     f.write(f"{i}\n")
# # f.close()
# c=[]
# for  i  in  text:
#     c.append(i.strip())
# print(c)
# f.close()


# def  a(x):
#     f=open(file=x,encoding="utf-8")
#     b=f.read()
#     print(b)
#     f.close()
#     return b
# a("a.txt")





