# 套接字作用：完成两个或多个应用程序之间的数据传输
# 模块
import socket
# 服务端
# 指定服务器的IP地址，监听端口号
ip_port=('127.0.0.1',6666)
# 建立一个套接字，为了服务器与客户端传输信息
s=socket.socket()
# 绑定服务地址和端口号
s.bind(ip_port)
# 设置最大连接数
s.listen(5)
# 提示服务端已经开启的信息
print('启动socket服务，等待客户端连接。。。')

# socket自动处理拥塞控制,持续开启服务，一直到手动关闭为止
conn,address=s.accept()

# # 处理客户端发过来的数据
# # # 第一步，接收客户端发送的数据
# # c_date=conn.recv(1024).decode('utf-8')
# # print(c_date)
# # print(address)
# # t=input('发送的数据').strip()
# # s.sendall(t.encode())
# # # 关闭连接
# # s.close()
while True:
    c_date = conn.recv(1024).decode('utf-8')
    print(f'客户端向服务器发送的内容是{c_date}')
    t = input('发送到客户端的信息').strip()
    if   t=="1":
        print('关闭服务器')
        break
    else:
        # 发
        # 1.找到客户端送信息给客户端
        # 2.使用sendall
        conn.send(t.encode())
# 关闭
s.close()