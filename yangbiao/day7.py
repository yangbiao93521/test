# python异常处理
# 1.错误
# 1.python语法错误：书写格式
# 2.代码逻辑：python解释器无法编译解释，导致python报错

# 2。异常
# 处理错误的过程叫异常捕获

# 3.try...except   最简单的异常处理

# try:
#    d=  1 / 0
# except OverflowError:
#     print("异常已经被处理了")
# except   ZeroDivisionError:
#     print("ZeroDivisionError")
# finally:
#     print("无论异常是否被处理，都会输出finally下面的代码")
# 4.try....except....finally



# try:
#    d=  1 / 0
# except OverflowError:
#     print("异常已经被处理了")
# except   ZeroDivisionError:
#     print("ZeroDivisionError")
# else:
#     print("不存在异常，执行else下面的代码")

# python  with
# with 的应用场合：主要是操作系统资源，建立连接，python线程、进程的关闭释放
# with  一种概念：上下文管理
# 写法：
with   open(file="a.txt",mode="r",encoding="utf-8")  as   a:
    b=a.read()
    print(b)




# python 正则表达式
# 正则模块  re
# 正则只能匹配字符串

import re
# .:一个点代表除了\n以外的所有字符，一个点代表一个字符
# *：匹配前面的字符0次或者多次
# +：匹配+前面的字符一次或者多次
# ？：匹配问号前面的字符0次或一次
# ^:匹配字符串以某个字符开头的
# $:匹配字符串以某个字符结尾的
#{m}：匹配花括号前面的字符出现的指定次数
# {m,n}:匹配花括号前面的字符的指定此时，最大m次，最小n次  mn之间不能有空格，尽可能取n次
# []:匹配括号内任意一个的字符串,每个字符只匹配一次   [a-z]26个小写字母  [A-Z]26个大写字母   -表示范围
# | ： 匹配左右的表达式
# \D:  匹配非十进制的数字的字符
# \d:匹配十进制的数字
# \s：匹配空白字符   包括   \t,\n,\f,\v
# \S:匹配非空白字符的任意字符
# ():匹配




# s="https://www.baidu.com"
# 编译正则表达式
# # x=re.compile("https://www.（.*？）com")
# 匹配正则  match(编译过的正则表达式，字符串）    匹配不成功  返回 None
# # res=re.match(x,s)
# ree.re.search(正则表达式，要匹配的字符串） 从左向右对整个字符串进行搜索匹配   匹配不到返回None
# # ree=re.search(x,s)
# print(res)
# print(res.group())
# rre=re.findall(正则表达式，要匹配的字符串)  从左往右对整个字符串进行搜索匹配    匹配的内容 保存在列表里 ，使用小括号时，仅仅匹配括号里面的内容
# # rre=re.findall(x,s)
# # print(rre)
# print(ree)
# print(ree.group())
# ret.re.
# #

# 贪婪模式
# .*
# 尽可能匹配到更多的字符
# 非贪婪模式
# .*?
# 匹配到字符就停止


g="hello  world"
# re.sub(正则表达式，要替换的字符，要匹配的字符串）
k=re.sub("l","kk",g)
print(k)

f="1234567890"
h=re.sub("",",",f,3)
print(h)
