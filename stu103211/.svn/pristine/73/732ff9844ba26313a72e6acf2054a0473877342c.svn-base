
import socket
import sys

messages = [ 'This is the message. ',
             'It will be sent ',
             'in parts.',
             ]
server_address = ('localhost', 10000)

socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          ]


print(sys.stderr, 'connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:
    for s in socks:
        print(sys.stderr, '%s: sending "%s"' % (s.getsockname(), message))
        s.send(message.encode()) #发送message

    for s in socks:
        data = s.recv(1024).decode()  #接受1024
        print (sys.stderr, '%s: received "%s"' % (s.getsockname(), data))
        if not data:  #无数据就关闭连接
            print (sys.stderr, 'closing socket', s.getsockname())
            s.close()