

#client
import socket
import hashlib
import op_client

def input_addr(count):
    for i in range(count):
        #input_IP_address = input("ftp服务器IP地址：")
        input_IP_address = "127.0.0.1"
        port = 10024
        ip_port = (input_IP_address, port)
        sk = socket.socket()
        try:
            sk.connect(ip_port)
            return sk
        except Exception:
            print("input the ftp server again...")

def auth(sk,count):
    for j in range(count):
        #进行用户验证：
        user_name = input("输入用户名：")
        password = input("输入密码：")
        #加密密码：
        p = hashlib.sha512()
        p.update(password.encode())
        p.hexdigest()
        #print(p.hexdigest())
        #把用户名和密码合成字符串
        user_and_passwd = "%s|%s" % (user_name, p.hexdigest())
        sk.send(user_and_passwd.encode())
        auth_ack = sk.recv(1024)
        if auth_ack.decode() == "AUTH_DONE":
            print("seccussful")
            return True
        elif auth_ack.decode() == "AUTH_FAILED":
            print("failed")
    else:
        return False


if __name__ == '__main__':
    sk = input_addr(3)
    auth_code = auth(sk,3)
    if auth_code:
        print("可以进行操作啦。。。")
        operate_obj =op_client.op_client(sk)  #实例化客户端操作
        while True:
            #发送操作：
            operate = input("ftp >").strip()
            if len(operate) == 0:continue    #输入空本次循环

            sk.send(operate.encode())
            if operate.lower() == 'bye':break  #输入bye退出
            #返回收到确认
            operate_ack = sk.recv(1024).decode()
            operate_ack_list = operate_ack.split("|")
            if operate_ack_list[0] == "done":
                sk.send("begin".encode())
                #使用反射执行操作方法
                if hasattr(operate_obj , operate.split()[0]):
                    func = getattr(operate_obj,operate.split()[0])
                    func(operate.split()[1])  #执行，并传入参数

            elif operate_ack_list[0] == "failed":
                print("cmd input wrong. again.")
                continue




