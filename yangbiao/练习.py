# import pymysql
# class  A(object):
#     def   __init__(self):
#         self.connect=pymysql.connect(
#             host='192.168.10.33',
#              port=3306,
#             user='root',
#             database='test',
#             charset='utf8',
#             password='123456'
#         )
#         self.cur=self.connect.cursor()
#     def b(self):
#         sql='create  table  n  (name   char(30))'
#         self.cur.execute(sql)
#     def  c(self):
#         sql1='insert  into  n   values ("zhangsan")'
#         self.cur.execute(sql1)
#     def   d(self):
#         sql2='select  * from   n'
#         i=self.cur.execute(sql2)
#         j=self.cur.fetchmany(size=1)
#         print(i,j)
#
# aa=A()
# # aa.b()
# # aa.c()
# aa.d()

# import xlrd
# import xlwt
# class  A(object):
#     def  __init__(self,name,num):
#         self.a=xlrd.open_workbook(filename=name)
#         self.b=self.a.sheet_by_name(num)   #根据索引取表
#         # self.d=self.a.sheet_by_index(num)   # 根据表名取表
#     def  c(self):
#         d=xlwt.Workbook()
#         f=d.add_sheet("表1")
#         f.write(0,0,"遮阳伞")
#         d.save("b.xls")
#
#
# bb=A('a.xls','表一')
# bb.c()


# import paramiko
# class  A(object):
#     a=paramiko.SSHClient()
#     a.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     def  __init__(self):
#         self.a.connect(
#         hostname='192.168.10.33',
#         port=22,
#         username='root',
#         password="123456"
#
#         )
#     def  b(self):
#         stdin, stdout, stderr = self.a.exec_command("ls -al")
#         k=print(stdout.read().decode())
#         return k
# aa=A()
# aa.b()

# import   paramiko
# class A(object):
#         b=paramiko.Transport(('192.168.10.33',22))
#         b.connect(username='root',password='123456')
#         c=paramiko.SFTPClient.from_transport(b)
#         def  d(self):
#             e='/root/105.sh'
#             f=r"E:\yangbiao\a.xls"
#             self.c.put(f,e)
# pp=A()
# pp.d()


# import pymysql
# import xlwt
# class  A(object):
#     def    __init__(self):
#         self.a=pymysql.connect(
#             host='192.168.10.33',
#             user='root',
#             password='123456',
#             port=3306,
#             charset='utf8',
#             database='test'
#         )
#         self.b=self.a.cursor()
#     def   cha(self):
#         sql='select * from  A '
#         self.b.execute(sql)
#         c=self.b.fetchall()
#         return c
#     def   cun(self):
#         e=self.cha()
#         f=xlwt.Workbook()
#         g = f.add_sheet("表一")
#         for  i  in   range(len(e)):
#                 for  j   in  range(len(e[i])):
#                     g.write(i,j,e[i][j])
#                     f.save("mmmm.xls")
#
# aa=A()
# aa.cun()

# a='123'
# b=a[::-1]
# d=0
# for   i,j   in   enumerate(b):
#     for   c  in  range(10):
#         if   str(c)==j:
#             break
#     d+=c*10**i
# print(d)


# class   A(object):
#     def  a(self):
#         x=input('请输入一串英文')
#         y=x.split(" ")
#         z=y[-1]
#         v=len(z)
#         return v
# aa=A()a
# print(aa.a())


a=8843*10**3
b=0.08
c=0
while   b<a:
    b=b*2
    c+=1
print(c)
