import socket
import pickle
import logging
#log_file = "ftpserver.log"
import op_server
user_file = op_server.file_operate("ftpuser_file.pkl")

IP_address = "127.0.0.1"
port = 10024
ip_port = (IP_address,port)



def auth(conn, count):
    for i in range(count):
            auth_recv = conn.recv(1024)
            user_and_passwd = auth_recv.decode().split("|")
            user_dict = user_file.file_read()
            if user_and_passwd[0] in user_dict and \
                user_dict.get(user_and_passwd[0]) == user_and_passwd[1]:
                conn.send("AUTH_DONE".encode())
                return True
            else:
                conn.send("AUTH_FAILED".encode())






if __name__ == '__main__':


    sk = socket.socket()
    sk.bind(ip_port)
    sk.listen(5)

    while True:
        print("ftp server is ready..")
        conn, addr = sk.accept()
        auth_res = auth(conn,3)


        if auth_res:
            print("开始接受客户端命令啦。。。")
            operate_obj =op_server.op_server(conn)
            while True:

                operate = conn.recv(1024).decode()
                if operate.strip().lower() == "bye":
                    break

                if hasattr(operate_obj , operate.split()[0]):
                    conn.send("done|".encode())
                    if conn.recv(1024).decode() =="begin":
                        func = getattr(operate_obj,operate.split()[0])
                        func(operate.split()[1])
                else:
                    conn.send("failed|".encode())

        conn.close()