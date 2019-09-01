# python发送邮件
# 模块  smtplib   email
import  smtplib
from email.mime.text  import  MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
# 设置服务器所需要的信息
mail_host='smtp.163.com'        #邮件服务器地址
mail_user="18783828252@163.com" # 用户名
mail_pass="yb93521"              #客户端授权码或者密码
mail_port=465                #设置服务器端口号
sender='18783828252@163.com'    #邮件发送者的地址
receivers=["liwei17681882504@163.com"]

zhuti="邮件的发送"     # 设置邮件主题
neirong='asdsadsadsad'     # # 编辑邮件正文
#
# # 三个参数：第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
# message=MIMEText(neirong,'plain','utf-8')
# # 发送邮件时写收件人，发件人，主题
# # Header（）:填写邮件头部
# # 发送方信息
# message['From']=Header(sender)
# # 接收方信息
# message['To']=Header(str(';'.join(receivers)))
# # 主题绑定
# message['Subject']=Header(zhuti)
#
# # 登录并发送邮件
# try:
#     # 第一步登录到自己邮箱
#     # smtpObj=smtplib.SMTP()
#     # 连接到服务器
#     # smtpObj.connect(mail_host,25)
#     smtpObj=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
#
# # 登录到服务器
#     smtpObj.login(user=mail_user,password=mail_pass)
# # 发送邮件以字符串的形式发送出去as_string()
#     smtpObj.sendmail(sender,receivers,message.as_string())
# # 发送邮件之后退出邮箱
#     smtpObj.quit()
#     print("success")
# except smtplib.SMTPException as  e:
#     print('erro',e)    #打印错误
#
# 添加一个MIMEMultipart类，处理正文及附件，添加到邮件里
message=MIMEMultipart()
message['From']=Header(sender)
# 接收方信息
message['To']=Header(str(';'.join(receivers)))
# 主题绑定
message['Subject']=Header(zhuti)

# 使用HTML格式的正文内容，添加附件
with  open('abc.html','r')  as f:
    content=f.read()
# 设置HTML格式参数
part1=MIMEText(content,'html','utf-8')

# 以下都是附件代码
with open('abc.txt','r') as   h:
    content2=h.read()
# 设置HTML格式参数
part2=MIMEText(content2,'plain','utf-8')
# 附件设置内容类型，方便起见，设置为二进制流
part2['Content-Type'] = 'application/octet-stream'
#设置附件头，添加文件名
part2['Content-Disposition'] = 'attachment;filename="abc.txt"'
# 添加照片附Content-Disposition'件
with open('1.png','rb')as  fp:
    picture=MIMEImage(fp.read())
picture['Content-Type']='application/octet-stream'


picture['Content-Disposition']='attachment;filename="1.png"'

# 将内容添加到邮件主体中attach(添加的内容）
message.attach(part1)
message.attach(part2)
message.attach(picture)





