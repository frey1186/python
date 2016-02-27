
import socket

sk = socket.socket()
sk.bind(("127.0.0.1",9999))
sk.listen(5)

while True:
    print("server is waiting...")
    conn,addr = sk.accept()
    client_data = conn.recv(1024)
    print(client_data.decode())
    conn.sendall("滚蛋.".encode())

    while True:
        try:
            recv = conn.recv(1024)
            if not recv:
                print(">> linux client closed...")
                break
            print("recv:",recv.decode())
        except Exception:
            print(">> windows client closed...")
            break
        conn.send(recv)

    conn.close()
