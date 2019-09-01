#指定代码# -*- coding: utf-8 -*-的编码方式
# print("hello world!")
# c = False
# if  c:
    # print("hello world!")
# else:
    # print ("条件为假")

# name =  input("请输入用户名")
# password = input("请输入密码")

# if   name == "杨彪":
    # if  password == "123456":
    # print("登陆成功")
# else:
    # print ("密码错误。登录失败")
# else:
    # print("用户名错误，登录失败")
# num_1 = 101
# num_2 = 5
# t = num_1//num_2
# print(t)

# 计算器   输入任意两个数进行运算，选择运算方式
# input()
# + - * /
# if
# a = int(input("数字"))
# b = int(input("数字"))
# c = input ("运算符")
# o=(a+b)
# p=(a-b)
# q=(a*b)
# j=(a/b)
# if   c=="+":
#      print(o)
# elif c=="-":
#     print(p)
# elif c=="*":
#     print(q)
# elif c=="/":
#     print(j)

# a=int(input("请输入一个成绩"))
# if  a>=90:
#     print("优秀")
# elif 80<=a<90:
#     print ("良好")
# elif 60<=a<80:
#     print ("及格")
# elif a<60:
#     print("不及格")

# x=100
# y=50
# z=30
# if   x>y  or  y>z:
#     print("x的值最大")
#
# if  not  x==100:
#     print("x不等于100")
# else:
#     print("not语句不成立")



# 判断三角形
# c=int(input("最长边"))
# b=int(input("中等边"))
# a=int(input("最短边"))
# c>b>a
# if  (a+b>c  and   a+c>b  and  a+c>b) or   (a-b<c and a-c<b and b-c<a):
#     print("这是一个三角形")
#     if   a*a+b*b>c*c:

#                 print("这是一个锐角三角形")
#     elif  a*a+b*b<c*c:
#                 print("这是一个钝角三角形")
#     elif  a*a+b*b==c*c:
#         print("这是一个直角三角形")
# else:
#     print("这不是一个三角形")


# a=int(input("输入一个数"))
# b=int(input("输入另一个数"))
# c=int(input("输入最后一个数字"))
# if    a>b>c:
#         print (f"{a}, {b}, {c}"  )
# elif  c>a>b:
#         print (c, a, b)
# elif   c>b>a:
#         print(c, b, a)
# elif   a>c>b:
#         print (a,c,b)
# elif   b>a>c:
#         print (b,a,c)
# elif    b>c>a:
#          print(b,c,a)



# str_1='hello'
# str_2="hello"
# str_3 ="""123456"""
# str_4=""
# str_5=str_1+str_2
# print("'str_5' \n" *5)
# print(str_3[0])
# # print (str_1,str_2,str_3,str_4)
# if    str_4:
#     print ("真")
# else:
#     print("假")
#
# l=len(str_3)
# print(l)
#
# a="hello"
# b="e"
# # print(a.title())
# # print (a.upper())
# print(b.swapcase())
# #
# print (a.startswith("b"))
# print(a.endswith("h"))
# name="博文"
# age=18
# c=f"我在的学校是{name},我今年{age}岁"
# print(c)
# d="我在的学校是{},我今年{}岁".format(name,age)
# print(d)
#
# # a="I konw I beautoiful"
# # b=a.split(" ",2)
# # print(b)
#
# # python使用input(),输入一段英文，每个英文单词以空格分隔，求最后一个单词的长度
# # a=input("请输入一串英文")
# # b=a.split(" ")
# # print(f"最后一个字符串的长度是：{len(b[-1])}")
#
# a="0o12"
# b="Bowenzhisheng"
# print(a.isdecimal())

#
#
# s="hello word"
# for  a   in   s:
# #     print(f"子字符是{a}")
#
#
# print(range(1,10))
# for  i   in  range(1,10):
#     print(i)

# print("九九乘法表")
# for   i    in    range(1,10):
#     for   j  in   range(1,i+1):
#         o=i*j
#         print(f"\t\t{j}*{i}={o}\t\t",end='')
#     print("\n")
#

# # 回文
# a=input("请输入一串字符")
# b=len(a)
# c=0
# for i in  range(b):
#     if  a[i]==a[-(i+1)]:
#         pass
#     else:
#         c=c+1
# if  c==0:
#      print("这是回文")
# else:
#     print (f"这不是回文{a}")

# 水仙花数
# for   a   in   range(100,1000):
#     b=a//100
#     c=a//10%10
#     d=a%10
#     if  b**3+c**3+d**3==a:
#         print(a)

# 5的阶乘之和
d=0
for a in range(1,6):
    c=1
    for   b  in  range(1,a+1):
        c=c*b
    d=d+c
print(d)

# #100以内质数之和
# c=0
# for a in range(1,101):
#     for b in range(2,101):
#         if a%b==0:
#             break
#     if  a==b:
#         c=c+a
# print(c)

# # 1000以内因数之和是其本身
# for  a  in   range(1,1000):
#     c=0
#     for b in range(1,a):
#         if  a%b==0:
#             c=c+b
#     if c==a:
#         print(a)

# #
# # a=["qwe",[1,2,3]]
# # a.append("python")
# # # print(a)
# #
# #
# # a=[1,2,3]
# # b=["qwe","qwe,""wqe","qwe"]
# # c=a+b
# # print(c)
#
# # a=[1,2,3]
# # # a[0]=4
# #
##
# a="123"
# print(list(a))
#
#随机输入一串字符，判断是否全是数字，判断首字母是大写的，并统计有多少个
# a=(input("请输入一串字符"))
# e=a.split(" ")
# b=len(e)
# c=0
# d=0
# for  f   in  range(b):
#         if   e[f].isdigit():
#             c=c+1
#         if   e[f].istitle():
#             d=d+1
# print(f"全是数字的有{c}个")
# print(f"首字母是大写的有{d}个")

# 选择排序法
# a=input("请输入一串数字")
# b=a.split(",")
# c=len(b)
# for  d   in  range(0,c):
#     for  e  in  range(d+1,c):
#         if  int(b[d])>int(b[e]):
#             b[d],b[e]=b[e],b[d]
# print(b)


# 冒泡排序法
# a=input("请输入一串数字")
# b=a.split(",")
# c=len(b)
# for   d in  range(c):
#     for  e in   range(c-1):
#         if  int(b[e])>int(b[e+1]):
#             b[e],b[e+1]=b[e+1],b[e]
# print(b)


# a=[1,2,3,4,5,6,7,]
# print(enumerate(a))
# for  i  in  enumerate(a):
#     print(i)


# a=input("输入一个商品")
# b=int(input("请输入购买数量"))
# c=["方便面","矿泉水","红茶"]
# d=["5","2","3"]
# for  e,f  in enumerate(c):
#     print(e,f)
#     if  a==f:
#         d[e]*b=z
#
#         print


# d={"a":[1,2,3],
#    "b":["p","p","m"]
#  }
# a=d.items()
# print(a)
# for  i,j in  a:
#     print(i,j)
#
# #
# f=len(d)
# print(f)
# seq=["1",2,3]
# d=dict.fromkeys(seq)
# print(d)
# d=dict.fromkeys(seq,"100亿")
# print(d)

# a={1:"q",2:"w"}
# b={1:"e",2:"r"}
# c=a.update(b)
# print(c)
# print(a)
#



# a=[1,2,3,3,4,2,1]
# b=dict.fromkeys(a)
# print(b)
# for   c   in   b:
#     print(c)

# a=[1,2,3,2,4,3,4,4]
# for   b  in a:
#     if  a.count(b)>=2:

#         a.remove(b)
#         print(a)
# print(a)
#
# # 待改进
# a=[1,3,2,3,4]
# for  c  in range(len(a)):
#     for  d   in  range(c+1,len(a)):
#         if    a[c]==a[d]:
#             a.remove(d)
# print(a)

# a=[1,2,3,4,1,2,3,4]
# b=[]
# for  x  in  a:
#     if  x  not  in  b:
#         b.append(x)
# print(b)


# a=input("输入一串字符串")
# b=input("输入另外一串字符串")
# c=a.split(",")
# d=b.split(",")
# i={}
# if   len(c)==len(d):
#     for g in range(len(c)):
#         i[c[g]]=d[g]
#     print(i)
# if  len(c)>len(d):
#     for h in range(len(c)):
#         if   h<=len(d)-1:
#             i[c[h]]=d[h]
#         else:
#             i[c[h]]="none"
#     print(i)
# if  len(c)<len(d):
#     for  o  in  range(len(d)):
#         if  o<len(c):
#             i[c[o]]=d[o]
#         else:
#             i["fg"]=d[o]
#     print(i)

#
#
# # a=("f",1,[1,2],{1:1000},(1,2))
# # b=(1,2,3)
# # print(a[1:3])
# # print(a[::-1])
# # print(len(a))
# # a=(1,2,3,4,5,6)
# # print(min(a))
# # print(max(a))
# # print(a.count(1))
# #
# # a=("f",1,[1,2],{1:1000},(1,2))
# # del a
# # print(a)
#
# # 1、求 key1 对应value的和
# # 2、求 python 对应的值，并将每个版本的首字符大写、尾字符大写输出
# s = {
#     "key1": [1000, 2000, 3000],
#     2019: [
#         "hello",
#         {"python": ['py2.x', 'py3.x']},
#     ],
# }
# a=s.get("key1")
# c=len(a)
# print(c)
# d=0
# for   e  in   range(c):
#     d=d+(a[e])
# print(d)
#
#
# e=s.get(2019)
# print(e)
# f=e[1]
# print(type(f))
#








# # 题目要求
# # 将类似/medal/201906/24/Cloth_Single_5.png的放到一个列表内
# # 将类似/medal/201906/24/Cloth_Single_5_Get.png的放到一个列表内
# s = '[Description("衣物挑战5kg")]@        /medal/201906/24/Cloth_Single_5.png         @        /medal/201906/24/Cloth_Single_5_Get.png     @            [Description("衣物挑战10kg")]@        /medal/201906/24/Cloth_Single_10.png        @        /medal/201906/24/Cloth_Single_10_Get.png    @            [Description("衣物挑战15kg")]@        /medal/201906/24/Cloth_Single_15.png       @        /medal/201906/24/Cloth_Single_15_Get.png   @            [Description("衣物挑战20kg")]@        /medal/201906/24/Cloth_Single_20.png       @        /medal/201906/24/Cloth_Single_20_Get.png    @           [Description("衣物挑战25kg以上")]@        /medal/201906/24/Cloth_Single_25.png        @        /medal/201906/24/Cloth_Single_25_Get.png   @            [Description("衣物累计50kg")]@        /medal/201906/24/Cloth_Sum_50.png           @        /medal/201906/24/Cloth_Sum_50_Get.png'
# a=s.split("@")
# b=[]
# c=[]
# for  e  in   a:
#     if   e.find("Get.png")!=-1:
#         b.append(e)
#     elif e.find("png")!=-1:
#         c.append(e)
# print(b)
# print(c)

# a={1,2,3,"qwe"}
# a.add("python")
# print(a)
# a.remove("python")
# print(a)

#
# a={1,2,3,4,5,6,7}
# b={5,6,7,8,9,10}
# c=a.union(b)
# print(c)
#

import  random       #随机数模块
# c=set()
# for   b  in  range(10):
#     a = random.randint(0, 1000)
#     c.add(a)
# print



#

# a=int(input("输入一个数"))
# # if   a%2!=0:
# #     print(f"这是一个奇数{a}")
# # # # #     print(f"这是一个偶数{a}")
# # # else:
# a=0.08
# b=8843*1000
# c=0
# while   a<b:
#     a=a*2
#     c=c+1
#     print(a)
# print(c)

# i=0
# j=0
# for   a   in  range(1,101):
#     if   a%2==0:
#         i=i+a
#     else:
#         j=j+a
# print(j-i)


#
# a="Then one day the mother eagle appeared at the top of the mountain cliff, with a big bowl of delicious food and she looked down at her baby. The baby looked up at the mother and cried 'Why did you abandon me? I'm going to die any minute. How could you do this to me?'"

# 统计字符串长度大于5的
# 将e全部替换成博文
# 截取第一个逗号前的所有单词，并将首字符大写
# 删除除包含英文o的单词
# b=a.split(" ")
# e=len(b)
# for  c  in  range(e):
#     if   len(b[c])>5:
#         print(b[c])
# f=a.replace("e","bowen")
# print(f)
# g=a.split(",")
# h=(g[0])
# i=h.title()
# print(i)
# q=[]
# for   j  in  range(e):
#     if  "o"    in   b[j]:
#         q.append(b[j])
# print(q)




# d = {
#     "data": {
#         "msg":
#         [
#             {
#                 "s_1": ["Jim", "男",  19, "175cm"],
#                 "country": "美国"
#             },
#             {
#                 "s_2": ["Kity", "女",  17, "165cm"],
#                 "country": "法国"
#             },
#             {
#                 "s_3": ["Tom", "男",  19, "173cm"],
#                 "country": "美国"
#             },
#             {
#                 "s_4": ["拖拉斯基", "男",  18, "180cm"],
#                 "country": "俄罗斯"
#             },
#             {
#                 "s_5": ["阿卡丽", "女",  17, "175cm"],
#                 "country": "乌克兰"
#             },
#             {
#                 "s_6": ["牙买稻子", "女",  18, "161cm"],
#                 "country": "日本"
#             },
#             {
#                 "s_7": ["龟田一郎", "男",  19, "175cm"],
#                 "country": "日本"
#             },
#             {
#                 "s_8": ["张三", "男",  20, "180cm"],
#                 "country": "中国"
#             },
#             {
#                 "s_9": ["李秀琴", "女",  19, "175cm"],
#                 "country": "中国"
#             },
#             {
#                 "s_10": ["宋仲基", "女",  19, "175cm"],
#                 "country": "韩国"
#             },
#             {
#                 "s_11": ["金正鞋", "男",  19, "168cm"],
#                 "country": "朝鲜"
#             },
#             {
#                 "s_12": ["卡列夫斯基", "男",  21, "190cm"],
#                 "country": "俄罗斯"
#             },
#         ]
#     },
# }
# a = d["data"]["msg"]
# print(a)
# for i in range(1, 13):
#     b = f"s_{i}"
#     s = a[i - 1][b]
#     print(s)
#     e = a[i - 1]["country"]
#     print(e)
#     s.append(e)
#     t = tuple(s)
#     print(t)
# 求国家个数
# 求所有学生的身高范围
# 求统计男女比例
# 求平均身高
# 查询身高在170到180之间的学生名字
# a=d["data"]
# print(a)
# b=a["msg"]
# print(b)
#



# a = input("输入商品名")
# b = input("购买数量")
# i = ['方便面','矿泉水']
# j = [100,200]
# for m,n in enumerate(i):
#     #print(m,n)
#     if n == a:
#         zongjia = j[m] * int(b)
#         print(f"商品名:{a},数量:{b},单价:{j[m]},总价:{zongjia}")
#         break
# else:
#     print("商品不存在")







# 设计一个商场的销售、会员充值系统
# 1、展示在售商品，包含商品名、价格、库存量
# 2、用户根据商品编号选择商品、输入购买数量
# 3、结账功能，用户不是会员按照原价结算、是会员按照会员等级进行打折
# 4、使用会员时，判断是否是会员，是会员展示帐户余额，会员帐户默认金额1000，计算帐户剩余金额
# 5、用户输入X或x结束操作

# m=input("进入商场inter>>>>>>")
# a=["啤酒","饮料","矿泉水","花生","瓜子","果丹皮"]
# b=[8,5,4,3,2,1]
# c=[20,50,40,18,39,128]
# huiyuan=1000
# while  True:
#     for ii in range(len(a)):
#         print(a[ii],b[ii],c[ii])
#     d=input("请输入商品名")
#     e=int(input("请输入购买数量"))
#     h = int(input("是否使用会员，不使用请输入1，使用请输入会员号"))
#     if   h==666:
#         for  i,j in  enumerate(a):
#             if  d==j:
#                 print("是黄金八五折会员，huiyuan=1000")
#                 zongjia=b[i]*e*0.85
#                 hh = c[i] - e
#                 c[i] = hh
#                 huiyuanyue=huiyuan-zongjia
#                 huiyuan=huiyuanyue
#                 print(f"商品名{d},数量{e},单价{b[i]},总价{zongjia}库存量{hh},会员余额{huiyuanyue}")
#     elif  h==1:
#         for i, j in enumerate(a):
#             if d == j:
#                 print("普通会员")
#                 zongjia = b[i] * e
#                 hh=c[i] - e
#                 c[i] = hh
#                 print(f"商品名{d},数量{e},单价{b[i]},总价{zongjia},库存量{hh}")
#     while  True:
#         v=input("是否继续购买？是的话请输入Q或者q，退出请输入X或者x")
#         if  v=="Q" or  v=="q":
#             break
#         elif  v=="X" or  v=="x":
#             exit()
#         else:
#             print("沙雕输入错误")



# class   A(object):
#     def   p(self,a,b):
#         for   i   in   range(a,b):
#             for   j   in  range(1,i+1):
#                 print(f"{j}*{i}={i*j}\t",end='')
#             print(f"\n")
# v=A()
# v.p(1,10)


#
# class   A(object):
#     def  __init__(self,x):
#         self.x=x
#     def   a(self):
#         d=[]

#         for   i   in  range(1,self.x):
#             c=0
#             for  j  in range(1,i+1):
#                 if  i%j==0:
#                     c=c+1
#             if  c==2:
#                 d.append(i)
#         return d
#
# class   B(A):
#     def  foo(self):
#         d=0
#         for  y  in  self.a():
#             d+=y
#         return  d
# c=B(100)
# print(c.foo())
#


