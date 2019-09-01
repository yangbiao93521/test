#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
import logging
import datetime
#日志文件夹/目录
LOG_DIR ='E:\\ybtest\\QQ\\logger\\'
#创建一个日志文件名字
a=LOG_DIR + str(datetime.datetime.now().date())+'.txt'
print(a)
#logging--->python定义日志的库
#定义日志输出的格式
formtter=logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')
print(formtter)
#logging两种输出方式
#1输出到pycharm控制台
c=logging.StreamHandler()
#添加日志的样式
c.setFormatter(formtter)
#2输出到文本
w=logging.FileHandler(a,encoding='utf-8')
#添加日志的样式
w.setFormatter(formtter)

def   get_logger(filename):
    #获取执行日志的脚本名字
    l=logging.getLogger(filename)
    #添加输出内容到控制台
    l.addHandler(c)
    #添加输出内容到文本
    l.addHandler(w)
    #定义日志的等级INFO-->最低等级
    l.setLevel(logging.INFO )
    return l

log = get_logger(filename='mylog.py')
log.info('asdk halkNMHTBYMS BO,V[P,CPVR ')
log.error('dsafdyb oifes nr')