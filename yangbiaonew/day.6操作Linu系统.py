# # 使用python操作Linux系统
# # 需要的模块：paramiko
# # 连接Linux，执行Linux命令
# # 支持文件上传下载
# import paramiko
# # 连接Linux系统
# # 建立连接第一步，创在一个sshcline对象
# # s=paramiko.SSHClient()
# # 建立连接第二步，允许信任Linux的主机，类似xshell 第一次连接的保存信息
# # s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 建立连接第三步，使用connect()远程连接Linux主机
# # s.connect(
# #     hostname="192.168.10.43",
# #     port =22,
# #     username="root",
# #     password="123456"
# # )
# # 执行Linux命令
# # exec_command(需要执行的命令)：执行命令的方法，命令需要写成字符串的类型
# # stdin,stdout,stderr=s.exec_command("ls -al")
# # # stdin(命令）,stdout（输出结果）,stderr（报错）
# # print(stdout.read().decode())
#
# # 文件下载、上传
# # SFTPClient(参数)：sftp客户端方法，参数：指的是之前建立的连接
# # 第二种连接Linux的方式，使用端口号连接  22
# # 套字节编程（网络编程）
# # Transport(参数)：端口号连接Linux，参数：包含IP地址 ，端口号的元组
# t=paramiko.Transport(("192.168.10.33",22))
# t.connect(username="root",password="123456")
# # SFTPClient.from_transport(参数)，sftp客户端方法，参数：指的是一个套字节服务端口   t
# sftp=paramiko.SFTPClient.from_transport(t)
# x1="/root/10.txt"   #linux 远程文件
# x2=r"E:\yangbiao"    #保存到本地的位置
# sftp.get(x1,x2)      #下载
#
# #put(本地文件，远程文件）：  上传
# sftp.put(x2,x1)
#
# #关闭连接、断开连接
# t.close()
# # s.close()

#scp

# import paramiko
# class   A(object):
#     s = paramiko.SSHClient()
#     s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     def  __init__(self):
#         s.connect(
#             hostname="192.168.10.43",
#             port=22,
#             username="root",
#             password="123456"
#         )

#python与系统的交互
# 系统包括Windows，Mac，Unix
# python内置模块——>python自带的，下载之后就有的   os库
import os
# import os
# 获取当前目录——>类似于Linux：pwd;  os.getcwd()
# a=os.getcwd()
# print(a)
#切换目录：os.chdir("dirname")
# os.chdir("E:\yangbiao\B")
# b=os.getcwd()
# print(b)
# 返回当前目录：os.curdir(）代表当前目录
os.chdir(os.curdir)
#返回上一级目录：os.pardir()代表上一级目录
# os.chdir(os.pardir)
# 获取操作系统的类型os.name
# nt代表Windows，“posix”
# n=os.name
# print(n)
# 创建多级目录A/a/c
# os.makedirs("aaa/bbb/ccc")
# 创建一个目录
# os.mkdir("ddd")
# 删除多个目录,只能删除空目录
# os.removedirs("aaa/bbb/ccc")
# 删除单个目录，只能删除空目录
# os.rmdir("ddd")
# 查看当前路径下所有的文件目录包括隐藏文件，类似Linux里面的ls  -al,返回的是一个列表
# v=os.listdir("E:\yangbiao")
# print(v)
# 对文件或者目录进行重命名
# os.rename("E:\yangbiao\B","E:\yangbiao\BB")
# 删除文件
# os.remove("E:\yangbiao\zc.xls")
# 执行系统命令
# a.os.popen("ls  -al")dd
# 目录树    ox.walk  类似  Linux里面的tree
# for  i   in  os.walk("E:\yangbiao"):
#     print(i)


# os.path类  对文件的操作
# 1.返回一个文件的绝对路径
# a=os.path.abspath("a.txt")
# # print(a)
# #2.返回文件的目录名
# b=os.path.dirname("E:\yangbiao\BB\bb.py")
# print(b)
# # 3.返回当前文件的目录
# c=os.path.basename("E:\yangbiao\BB.bb.py")
# print(c)
# # 4.判断文件是否存在——>返回布尔值
# d=os.path.exists("E:\yangbiao")
# print(d)
# # 5.判断是否是目录
# e=os.path.isdir("BB")
# print(e)
# # 6.判断是否是文件
# f=os.path.isfile("73.xls")
# print(f)
# # 7.判断是否为链接文件
# g=os.path.islink("73.xls")
# print(g)
# # 8.文件路径拼接
# h=os.path.join("E:\yangbiao\BB",'E:\yangbiao\1.py')
# print(h)
# # 9.文件路径分离   将前一个文件/目录与最后一个进行分割，返回一个元组
# i=os.path.split("E:\yangbiao\b.xlsx")
# print(i)
# # 10.分割文件的后缀名   返回一个元组
# j=os.path.splitext("E:\yangbiao\b.xlsx")
# print(j)
#
# # 统计当前目录下有多少个文件.目录
# import paramiko
# class   A(object):
#     s = paramiko.SSHClient()
#     s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     def  __init__(self):
#         self.s.connect(
#             hostname="192.168.10.33",
#             port=22,
#             username="root",
#             password="123456"
#         )
#     def  b(self):
#         stdin, stdout, stderr = self.s.exec_command("ls -al")
#         a=print(stdout.read().decode())
#         return a
# aa=A()
# aa.b()



#
# aa = os.getcwd()
# print(aa)
# bb=os.listdir("E:\yangbiao")
# print(bb)
# cc=len(bb)
# print(cc)
# m=0
# n=0
# for i in  range(cc):
#         if  os.path.isdir(bb[i]):
#             m+=1
#         if   os.path.isfile(bb[i]):
#             n+=1
# print(m)
# print(n)
#
#
# class   A(object):
#     i=os.listdir("E:\yangbiao")
#     def  __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def count(self):
#         for  j   in  self.i:
#             if   os.path.isdir(j):
#                 self.x+=1
#             if  os.path.isfile(j):
#                 self.y+=1
#         return self.x,self.y
# cc=A(0,0)
# print(cc.count())
#

#python对时间的操作
# time
# 1.睡眠sleep（浮点数）   浮点数、整数   单位秒
# import time
# print("睡眠之前")
# time.sleep(5)
# print("睡眠之后")
# 2.CPU 运算代码的时间
# print(time.clock())
# 3.本地时间
# print(time.ctime())
# print(time.asctime())
# print(time.localtime())#输出时间的详细信息
# 4.格式化输出时间
# print(time.strftime("%A,%d"))
# 5.根据格式解析表示时间的字符串
# print(time.strptime("30 Nov 00","%d %b %y"))
# 7.距离计算机元年过去的秒的综合
# print(time.time())

# #python对日期的操作
# # datetime
# from   datetime import    *
# # 1.获取当前时间、日期
# # print(datetime.now())
# # 2.获取指定的时间，日期
# # print(datetime(1994,11,9,12,1,1))
# # 3.字符串转日期
# t=datetime.strptime("1994-11-09 12:01:01","%Y-%m-%d %H:%M:%S")
# # 4.日期转字符串
#
# # 5.日期的加减
# now=datetime.now ()
# q=now+timedelta(days= 5)
# print(q)
# # 6.获取当前的日期
# print(date.today())
# print(date(1994,10,2).ctime())
# # 7.对日期进行加减
# f=date.today()-timedelta(days=5)
# print(f)

