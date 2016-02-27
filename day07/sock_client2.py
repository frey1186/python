
import socket

sk = socket.socket()
sk.connect(("127.0.0.1",9999))

sk.sendall("我来啦....".encode())
server_data = sk.recv(1024)
print(server_data.decode())

while True:
    msg_input = input(">>:").encode()
    sk.send(msg_input)
    ser_recv = sk.recv(1024)
    print(ser_recv.decode())

sk.close()