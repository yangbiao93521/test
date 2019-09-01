import random
import re
import requests
import xlwt
import pymysql
class  Zhilian(object):
    def   get(self):
        a=requests.get(r"https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试&kt=3&=0&_v=0.94112276&x-zp-page-request-id=d8da32811392441e8c79108a64a7cb24-1562659656311-780091&x-zp-client-id=151a2d94-4916-46c7-980d-87c30f711422",headers={"User_Agent":'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'})
        c=a.text
        b=re.compile(r'"jobName":"(.*?)".*?"company":{"name":"(.*?)".*?"size":{"name":"(.*?)"}.*?"display":"(.*?)"}.*?"salary":"(.*?)"',re.S)
        e=re.findall(b,c)
        print(len(e))
        return e
    # def  biao(self):
    #     t=self.get()
    #     o=xlwt.Workbook()
    #     p=o.add_sheet("biao1")
    #     for    i  in   range(len(t)):
    #         for   j   in   range(len(t[i])):
    #             p.write(i,j,t[i][j])
    #     o.save("zhilian.xls")
    def shujuku(self):
        h=self.get()
        x = pymysql.connect(
        host = '192.168.10.43',
        port = 3306,
        user = "root",
        password = "123456",
        charset = 'utf8',
        database = "test"
    )
        y=x.cursor()
        sql2="create  table  B  (zhiwu  char(100),gonsi  char(100),renshu  char(100),diqu  char(100),xinzi  char(100))"
        y.execute(sql2)
        for   i  in   h:
            sql3=f"insert  into  B  values{i}"
            y.execute(sql3)
        x.commit()
aa=Zhilian()
# print(aa.get())
aa.shujuku()

















# import json
# json.loads("想转的内容")#将json转换成python字典
# json.dumps("想转的内容")#将python字典转换成json字符串