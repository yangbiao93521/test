# pip  python的第三方包下载工具，下载python的第三方包
# 什么是python的包
# python脚本文件的汇总集合被称为包
#pip命令
# pip  install   报名     下载
# pip  list   查找pip下载过的所有包



import  pymysql
# "# # 第一步链接数据库
# connect   =  pymysql.connect(
#     host="192.168.10.39",   #数据库所在的主机IP地址/域名（云服务器）
#     port=3306,              # mysql的端口号
#     user="root",            #mysql的用户名
#     password="123456",
#     charset="utf8",)
#     # database="库名"#指定数据库，不写的话使用所有的数据库
# cur=connect.cursor()    #游标：类似于MySQL   >命令行模式
# # sql="create   database   stu1903"
# # sql="show  databases"
d = {
    "data": {
        "msg":
            [
                {
                    "s_1": ["Jim", "男", 19, "175cm"],
                    "country": "美国"
                },
                {
                    "s_2": ["Kity", "女", 17, "165cm"],
                    "country": "法国"
                },
                {
                    "s_3": ["Tom", "男", 19, "173cm"],
                    "country": "美国"
                },
                {
                    "s_4": ["拖拉斯基", "男", 18, "180cm"],
                    "country": "俄罗斯"
                },
                {
                    "s_5": ["阿卡丽", "女", 17, "175cm"],
                    "country": "乌克兰"
                },
                {
                    "s_6": ["牙买稻子", "女", 18, "161cm"],
                    "country": "日本"
                },
                {
                    "s_7": ["龟田一郎", "男", 19, "175cm"],
                    "country": "日本"
                },
                {
                    "s_8": ["张三", "男", 20, "180cm"],
                    "country": "中国"
                },
                {
                    "s_9": ["李秀琴", "女", 19, "175cm"],
                    "country": "中国"
                },
                {
                    "s_10": ["宋仲基", "女", 19, "175cm"],
                    "country": "韩国"
                },
                {
                    "s_11": ["金正鞋", "男", 19, "168cm"],
                    "country": "朝鲜"
                },
                {
                    "s_12": ["卡列夫斯基", "男", 21, "190cm"],
                    "country": "俄罗斯"
                },
            ]
    },
}
#执行SQL语句
# cur.execute(sql)
# print(cur.execute(sql))


class   Usemysql(object):
    def  __init__(self):
        self.connect=pymysql.connect(
            host="192.168.10.43",
            port=3306,
            user="root",
            password="123456",
            charset="utf8"
        )
        self.cur = self.connect.cursor()
    def  create_database(self):
        cur=self.connect.cursor()
        sql="create   database   stu110"
        cur.execute(sql)
    def   create_tables(self):   #普通方法
        cur=self.connect.cursor()
        sq="use   stu110"
        sw="create   table  c  (name  char(10),sex  int(10),xingbie  char(10),shengao  int(10),guojia  char(30))"
        cur.execute(sq)
        cur.execute(sw)
    def  insert_tables(self):
        a = d["data"]["msg"]
        for i in range(1, 13):
            b = f"s_{i}"
            s = a[i - 1][b]
            e = a[i - 1]["country"]
            s.append(e)
            t = tuple(s)
            cur = self.connect.cursor()
            ss="use  stu110"
            se=f"insert  into  c  values  {t}"
            cur.execute(ss)
            cur.execute(se)
            #保存数据到数据库
            self.connect.commit()
    def cha(self):
        cur = self.connect.cursor()
        sq = "use   stu110"
        cur.execute(sq)
        sql ="select * from  c "
        # a=cur.execute(sql)
        b=cur.fetchall()
        #fetchall()  返回的是一个元组
        #fetchall(size=1)查询指定条
        #fetchone()查询一条
        # print(a)
        print(b)
    def   close(self):
#与数据库的断开连接
        self.connect.close()

my=Usemysql()
my.create_database()
my.create_tables()
my.insert_tables()
my.cha()

