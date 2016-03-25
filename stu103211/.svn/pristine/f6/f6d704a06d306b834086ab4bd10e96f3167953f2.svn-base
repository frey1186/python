import socket
import select
import queue
import sys

server = socket.socket()  #创建一个socket对象
server.setblocking(0)    #设置为不阻塞

server_address = ("localhost",10000)  #定义主机和端口元祖
print(sys.stderr,"start up on %s port %s." % server_address)  #打印信息
server.bind(server_address)  #绑定端口

server.listen(5)  #监听，最大链接数为5

inputs = [server]  #为select定义输入
outputs = []       #为select定义输出
massage_queue = {} #定义消息队列，空字典

while inputs:
    print("\nwaiting for the next event...")
    #实例化select对象
    readable,writable,exceptional = select.select(inputs,outputs,inputs)
    #循环可读列表：
    for s in readable:
        if s is server:  #如果是server，就是socket对象
            connect, client_address = s.accept()  #接受客户端连接
            print("new connection from %s" % client_address[0]) #打印信息
            connect.setblocking(0)  #设置为非阻塞
            massage_queue[connect] = queue.Queue()  #为连接定义一个队列，并存放到信息队列中
        else:  #如果不是对象，就是数据
            data = s.recv(1024)  #接受1024字节数据
            if data:#如果有数据
                print(sys.stderr,"recved %s from %s." % (data, s.getpeername()))
                massage_queue[s].put(data)  #队列中增加数据
                if s not in outputs: #如果不在输出列表中，就在输出列表中增加
                    outputs.append(s)
            else:#否则：
                print("closing %s after read no data." % client_address[0])
                if s in outputs:  #如果在输出列表中，就删除
                    outputs.remove(s)
                inputs.remove(s)   #删除输入列表中的数据
                s.close(s)    #关闭连接
                del massage_queue[s]  #删除消息队列中的数据
    
    
    for s in writable:
        try:
            next_msg = massage_queue[s].get_nowait()  #获取队列中的值
        except queue.Empty:
            print('output queue for', s.getpeername(), 'is empty')
            outputs.remove(s)  #在输出列表中删除
        else:
            print('sending "%s" to %s' % (next_msg, s.getpeername())) #
            s.send(next_msg)  #发送值
            
    for s in exceptional:
        print('handling exceptional condition for', s.getpeername()) #打印远程端口
        inputs.remove(s)  #删除输入列表中的数据
        if s in outputs:  #如果在数据列表中存在，就删除
            outputs.remove(s)
        s.close()  #关闭连接
        del massage_queue[s]    #删除字典item
                                                 
