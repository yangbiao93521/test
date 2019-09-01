# # python操作excel表格
# # 1.python读取excle表格中的数据——需要使用第三方包：xlrd
#
# import xlrd
# # 打开Excel文件
# d=xlrd.open_workbook(filename="a.xlsx")
# # 获取Excel表    返回的是一个包含Excel的列表
# # 假设文件中存在两个Excel表，那么列表中["sheet
# 1"，"sheet2"]
# table=d.sheets()[0]
# # 获取表中的数据   row_valies():获取整行的数据   必须指定获取的行号
# x=table.row_values(1,0)
# # print(x)
# # 获取某个单元格的值  先通过row()获取某一行——>返回一个列表
# # 再通过列表的索引获取到元素——>.value获取到具体的值
# dan=table.row(0)[0].value
# # print(dan)
# # 获取整列的值   先通过col获取某一列——>返回一个列表
# # 再通过列表的索引获取到元素——>.value获取到具体的值
# s=table.col(0)[0].value
# # print(s)
# v=table.cell(0,1).value
# # print(v)
# # 获取行数
# f=table.nrows
# # print(f)
# # 获取列数
# h=table.ncols
# # print(h)
# # 通过行数获取所有的值
# for  i  in  range(f):
#     print(table.row_values(i))
# # 通过列数获取所有的值
# b=table.col_values(1)    # 获取整列的数据
# for   i  in range(h):
#     print(table.col_values(i))
#
# # 输出excle表的名字
# # d: 代表的是的打开exlce  文件
# print(d.sheet_names())
# # 通过索引获取工作表
# # 假设一个文件存在两个表sheet1.sheet2
# # sheet_by_index():  0 ——>打开的就是sheet1文件在内存的位置
# table=d.sheet_by_index(0)
# print(table)
#
import xlrd
class  Escel(object):
    def   __init__(self,name,num):
        # 第一步打开文件
        self.d=xlrd.open_workbook(filename=name)
        # 使用某一张表
        self.t=self.d.sheet_by_index(num)
    # 获取一张表中所有的数据
    def  data(self):
        # 将所有数据装到一个空列表中
        e=[]
        n=self.t.nrows
        for  i   in   range(n):
            print(self.t.row_values(i))
            e.append(self.t.row_values(i))
        return e
dui=Escel("a.xlsx",0)
print(dui.data())

import xlrd
class   Txt(Escel):
    def  write_data(self):
        f=open(file="a.txt",mode="w",encoding="utf_8")
        shuju=dui.data()
        for  i   in   shuju:
            print(i)
            for  j  in  i:
                f.write(str(j)+"\t")
            f.write("\n")
ti=Txt("a.xlsx",0)
ti.write_data()

#
#
# # python向Excel文件中写入数据
# import xlwt
# # 新建一个Excel文件
# d=xlwt.Workbook()
# # 新建一个Excel表  add_sheet(工作表的名字）必填
# table=d.add_sheet("表1")
# # 写入数据到Excel
# # 一次写入一个单元格
# table.write(0,0,"张三")
# # 保存文件    save(文件名)必填
# d.save("73.xls")



# import xlwt
# class   A(object):
#     c = xlwt.Workbook()
#     b = c.add_sheet("表一")
#     def   __init__(self,name,num):
#         self.name=name
#         self.num=num
#     def   xieru(self,x,y,z):
#         self.b.write(x,y,z)
#         self.c.save(self.name)
# u=A("a.xls",0)
# u.xieru(0,0,"zhangsan")
# #
#
# import xlwt
# class M(object):
#     c = xlwt.Workbook()
#     table = c.add_sheet("表一")
#     def __init__(self,x,y,name,sex,age):
#         self.x = x
#         self.y = y
#         self.name = name
#         self.sex = sex
#         self.age = age
#     def sj(self):
#         t = []
#         g = self.y
#         t.append(self.name,)
#         t.append(self.sex)
#         t.append(self.age)
#         for i in range(len(t)):
#             self.table.write(g,i,t[i])
#             self.c.save(self.x)

# n = M("zc.xls",0,"孙t","nv",23)
# n.sj()

# 九九乘法表写入Excel表格
import xlwt
class  A(object):
    a = xlwt.Workbook()
    b = a.add_sheet("biao1")
    def   __init__(self,x):
        self.x=x
    def  chengfabiao(self):
        for i in  range(1,self.x):
            for j in range(1,i+1):
                self.b.write(i-1,j-1,f"{j}*{i}={i*j}")
        self.a.save("e.xls")
c=A(10)
c.chengfabiao()






