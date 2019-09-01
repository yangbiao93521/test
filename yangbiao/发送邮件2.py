
#   python 发送电子邮件   使用到的模块    smtplib   email
import  smtplib
from email.mime.text  import  MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
#设置服务器所需要的信息
mail_host = "smtp.163.com"                                      #  邮件服务器地址
mail_user = "guohg18991002302@163.com"                            #  用户名
mail_pass = "guo18991002302"                                   #客户端授权码或者密码
mail_port = 465                                                    #设置服务器端口号
sender = "guohg18991002302@163.com"                                           #  邮件发送方的地址
receviers = ["liwei17681882504@163.com" , "18783828252@163.com" ]                                    #  邮件接收方的地址

#  设置邮件信息如下
a = "python测试邮件"                   #  设置邮件主题
a1 = "这是我使用python发送的邮件"       # 设置邮件正文
s = MIMEText(a1,'plain','utf-8')       #三个参数：第一个为文本内容，第二个设置文本格式，第三个设置编码方式

#  发送邮件是填写收件人，发件人，主题
# header（）： 填写邮件头部
s['From'] = Header(sender)                              #  发送方信息
s["To"] = Header(str(";".join(receviers)))       # 接收方信息
s["Subject"] = Header(a)                         #  主题绑定

#  登录并发送邮箱
try:
    # 第一步，登录到自己的邮箱   #  一种是不使用授权密码
    s1 = smtplib.SMTP_SSL(host=mail_host,port=mail_port)
    # 第二步，输密码登录邮箱
    s1.login(user=mail_user,password=mail_pass)
    # 第三步,发送邮件，as_string()    以字符串的形式发送出去
    s1.sendmail(sender,receviers,s.as_string())
    #  第四步，发送邮件之后退出邮箱
    s1.quit()
    print("发送成功，退出邮箱")
except smtplib.SMTPException as e :
    print("登录失败")