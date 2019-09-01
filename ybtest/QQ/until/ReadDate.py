#!/usr/bin/python
#-*-coding:utf8-*-
#美好生活从python开始！
with  open(file='E:\ybtest\QQ\data\data_1',mode='r',encoding='utf8')as   f:
    shuju=f.read().split(';')
print(shuju)
s=[]
for  i  in  shuju:
    k=i.replace("\n","").split(',')
    s.append(tuple(k))
print(s)
