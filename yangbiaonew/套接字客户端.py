# 客户端
import socket
# 指定客户端IP，目的端口号
ip_port=('127.0.0.1',6666)
# 创建一个套接字，目的是接受服务器发送的数据
c=socket.socket()
# 连接服务器
c.connect(ip_port)
# 发送数据到服务器，接收服务器数据
# t=input('发送的数据').strip()
# # 发送
# c.sendall(t.encode())

while True:
    t = input('发送的数据').strip()
    # 设置一个条件跳出死循环
    if   t=="1":
        break
    else:
        print("发送信息到服务器")
        c.send(t.encode())
        #处理服务器已经发送到客户端上的信息
        s_date =c.recv(1024).decode('utf-8')
        print(s_date)

# 关闭连接
c.close()
