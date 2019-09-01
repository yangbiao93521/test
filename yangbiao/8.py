import re
import requests

respose=requests.get('http://www.xiaohuar.com/v/')
# print(respose.status_code)# 响应的状态码
# print(respose.content)  #返回字节信息
# print(respose.text)  #返回文本内容
urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
url=urls[5]
result=requests.get(url)
mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]

video=requests.get(mp4_url)

with open('D:\\b.mp4','wb') as f:
    f.write(video.content)


# # python 爬虫
# # 有目的的获取网络中的资源
d={"User-Agent":    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
# # 发送URL请求
# rep=requests.get("https://www.fpzw.com/xiaoshuo/88/88413/17355844.html",headers=d)
# # 接收html文本
# res=rep.content.decode("gbk")

# print(res)
# s1=re.compile("</script>&nbsp;&nbsp;&nbsp;&nbsp(.*?)</p></div>")
# neirong=re.findall(s1,res)
# # print(neirong)
# b=neirong[0]
# a=re.sub('<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;','',b)
# print(a)


rep=requests.get('https://www.fpzw.com/xiaoshuo/88/88413/',headers=d)
res=rep.content.decode("gbk")
s1=re.compile('<dd><a href="(.*?).html">(.*?)</a></dd>')
b=re.findall(s1,res)
# print(b[0][0])
for    i   in  range(len(b)):
    rew = requests.get(f"https://www.fpzw.com/xiaoshuo/88/88413/{b[i][0]}.html",headers=d)
    rey = rew.content.decode("gbk")
    s2=re.compile("</script>&nbsp;&nbsp;&nbsp;&nbsp(.*?)</p></div>")
    neirong = re.findall(s2, rey)
    c = b[i][1]
    a=re.sub('<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;','',neirong[0])
    with open(file=r'C:\Users\YangB\Desktop\小说.txt',mode="a",encoding="utf-8")  as  v:
        v.write(f"{c}\n")
        v.write(f"str({a})\n")
