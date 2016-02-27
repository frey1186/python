
import socket

sk = socket.socket()
sk.connect(("127.0.0.1",9999))

sk.sendall("我来啦....".encode())
server_data = sk.recv(1024)
print(server_data.decode())
sk.close()