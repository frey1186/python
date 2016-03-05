
import socket
HOST = "127.0.0.1"
PORT = 55011

sk = socket.socket()
sk.connect((HOST,PORT))
while True:
    cmd = input(">>").strip()
    if not cmd:
        continue
    sk.send(cmd.encode())
    server_data = sk.recv(1024)
    print("server recv :",server_data.decode())

