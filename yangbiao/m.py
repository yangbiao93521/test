import requests,re

i = {
    "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
}
# # 发送url请求
req = requests.get('https://www.fpzw.com/xiaoshuo/88/88413',headers=i)
# # 接收html文本
res = req.content.decode('gbk')




class Pxs(object):
    req = requests.get('https://www.fpzw.com/xiaoshuo/88/88413',headers=i)
    res = req.content.decode('gbk')
    s3 = re.compile('<dd><a href="(.*?).html">(.*?)</a></dd>')
    urls = re.findall(s3,res)
    print(urls)
    # def paxs(self):
    #     k = {}
    #     for j in self.urls:
    #         url = f'https://www.fpzw.com/xiaoshuo/88/88413/{j[0]}.html'
    #         mu = j[1]
    #         k[mu] = url
    #
#             ml = requests.get(f'{k[mu]}',headers=i)
#             wz = ml.content.decode('gbk')
#             s1 = re.compile('<h2>(.*?)</h2>')
#             bt = re.findall(s1,wz)
#             s2 = re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</p>')
#             nr = re.findall(s2,wz)
#             neirong = str(nr).split("<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;")
#             with open(file=r"C:\Users\SunGX\Desktop\棋魂.txt",mode="a",encoding="utf8") as m:
#                 m.write(f'{str(bt)}\n')
#                 m.write(f'{neirong}\n')
#
# a = Pxs()
# a.paxs()