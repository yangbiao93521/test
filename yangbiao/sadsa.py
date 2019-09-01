# import re,requests
# import random
# user_agent = [
#     "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
#     "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
#     "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
#     "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
#     "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
#     "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
#     "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
#     "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
#     "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
#     "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
#     "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
#     "UCWEB7.0.2.37/28/999",
#     "NOKIA5700/ UCWEB7.0.2.37/28/999",
#     "Openwave/ UCWEB7.0.2.37/28/999",
#     "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
#     # iPhone 6：
# 	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
#
# ]
# o=random.randint(0,36)
# class  A(object):
#     def   shouji(self):
#         url=requests.get('http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html',headers={"User_Agent":user_agent[o]})
#         html=url.content.decode('gbk')
#         return html
#
#     def  tu(self):
#         a=self.shouji()
#         # print(a)
#         b=re.compile('src="(.*?)" alt=.*?</a>')
#         d=b.findall(a)
#         for i  in  range(len(d)):
#             url1=requests.get(d[i],headers={"User_Agent":user_agent[o]})
#             html2=url1.content
#             with  open(rf'F:\新建文件夹\{i}.jpg','wb')  as  m:
#                 m.write(html2)
# aa=A()
# aa.tu()

#一千以内的完数（一个数的所有因数之和是其本身）
# 方法1
# class   A(object):
#     def   a(self):
#         for   i   in  range(1,1001):
#             b=0
#             for   j  in  range(1,i):
#                 if   i%j==0:
#                     b+=j
#             if   b==i:
#                 print(i)
# aa=A()
# aa.a()
#方法2
# a=1
# while   a<1000:
#     b=1
#     c=0
#     while  b<a:
#         if   a%b==0:
#             c=c+b
#         b+=1
#     if   c==a:
#         print(a)
#     a+=1

# 去除列表中重复的元素
# h = [1,2,2,3,4,3,4,4]
# a=[]
# for  i  in  h:
#     if    i  not  in   a:
#         a.append(i)
# print(a)


# class   A(object):
#     def  a(self,*args):
#         c=args
#         b=list(c)
#         print(b[0])
#         print(len(b))
#         for   i  in    range(0,len(b)):
#             for   j  in  range(i+1,len(b)):
#                 if   b[i]>b[j]:
#                     b[i],b[j]=b[j],b[i]
#         print(b)
#         return b
# aa=A()
# aa.a((2),(5),(1),(66),(1))

# class   A(object):
#     def   a(self):
#         a=input("dsad")
#         b=a.split(",")
#         for   i  in range(0,len(b)):
#             for   j  in range(0,len(b)-1):
#                 if  int(b[j])>int(b[j+1]):
#                     b[j],b[j+1]=b[j+1],b[j]
#         print(b)
#         return b
# aa=A()
# aa.a()

# class   A(object):
#     def  a(self):
#         c=0
#         for  i  in   range(1,6):
#             b=1
#             for  j  in range(1,i+1):
#                 b=b*j
#             c=b+c
#         print(c)
#         return c
# aa=A()
# aa.a()

# class A(object):
#     def zx(self):
#         e = 0
#         r = 1
#         b=0
#         for i in range(1,6):
#             r = r * i
#             e += r
#
#             b+=e
#         return b
# a = A()
# print(a.zx())






# class  A(object):
#     def  a(self):
#         h=[]
#         for  i  in range(100,1000):
#             b=i//100
#             c=i//10%10
#             d=i%10
#             if    b**3+c**3+d**3==i:
#                 h.append(i)
#         return h
# aa=A()
# print(aa.a())


# class   A(object):
#     def  a(self):
#         b=0
#         for  i  in range(1,100):
#             if   i%2==0:
#                 b=b-i
#             if  i%2!=0:
#                 b=b+id
#         return b
# aa=A()
# print(aa.a())


# a='12345'
# b=a[::-1]
# d=0
# for   i,j  in  enumerate(b):
#     print(i,j)
#     for   k  in range(10):
#         if  str(k)==j:
#             c=k*10**i
#             d=d+c
# print(d)

# a='123'
# eval(a)
# print(a)
#






# a=1
# while   a<10:
#     b = 1
#     while   b<a+1:
#         print(f"{b}*{a}={a*b}""\t",end="")
#         b+=1
#     print()
#     a+=1


# 组成不同的三位数，个位十位百位数字不能相等
# a=[1,2,3,4]
# d=0
# for   i   in    a:
#      for    j   in    a:
#          for   o  in    a:
#              if   i!=j    and  i!=o and   j!=o       :
#                  c=i*100+j*10+o
#                  d+=1
#                  print(c)
# print(d)



# class  A(object):
#     def  a(self,b):
#         c=reversed(b)
#         if   b==c:
#             print("zheshihuiwen")
#         else:
#             print('这不是回文')
# aa=A()
# aa.a('12321')




