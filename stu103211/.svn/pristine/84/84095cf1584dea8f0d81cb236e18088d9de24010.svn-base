import os
import socketserver
import configparser

import command_handler

config_file = "../conf/ftpd.conf"
ftpuser_file = "../conf/ftpuser.pkl"

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
home_dir = os.path.join(base_dir,"var","users")

import pickle
class file_operate(object):
    def __init__(self, file_name):
        self.file_name = file_name

    #读文件,转化为python对象
    def file_read(self):
        fr = open(self.file_name, "rb")
        obj = pickle.load(fr)
        fr.close()
        return obj

    #将python对象写到文件中
    def file_write(self, obj):
        fw = open(self.file_name, "wb")
        pickle.dump(obj, fw)
        fw.close()

class FtpRequestHandler(socketserver.BaseRequestHandler):

    # def __init__(self,request,client_address,server):
    #     socketserver.BaseRequestHandler.__init__(self, request,client_address,server)
    response_code = {  #respinse|200|n/a|n/a
        '200': "Pass authentication!",
        '201': "Wrong username or password",
        '202': "FTP Command does not exist",
        '203': "File or directory doesn't exist",
        '204': "File is existed",
        '205': "directory is existed",

        '206': "There is no args behind the ftp command",

        '300': "Ready to send file to client",
        '301': "Client  is ready... ",
        '302': "ftp server is ready....",
        '303': "Client ready to receive file data",
        '304': "Client get file done.",
        '305': "Server get file done.",
        '306': "Server check file md5 done.",
        '307': "Server check file md5 failed.",

    }

    def handle(self):

        retry_times = 3  #最大重试次数
        retry_count = 0  #重试次数
        login_flag = False
        command_obj = command_handler.FtpCommandHandler(self.request)
        while True:
            recv_data = self.request.recv(1024)
            recv_list = recv_data.decode().split("|")
            if recv_list[0] == "auth":
                retry_count += 1  #重试次数+1
                if retry_count > retry_times:
                    break   #

                user_file = file_operate(ftpuser_file)
                user_dict = user_file.file_read()
                # user_dict = {
                #     #用户名：密码，配额1024M，登录标签
                #     "felo":["5f4dcc3b5aa765d61d8327deb882cf99",1024,False],
                #     "yang":["5f4dcc3b5aa765d61d8327deb882cf99",100,False],
                # }


                user_and_passwd = recv_list[1].split(",")
                if user_and_passwd[0] in user_dict:
                    if user_dict.get(user_and_passwd[0])[0] == user_and_passwd[1]:
                        self.request.send("response|200|n/a|n/a".encode())
                        login_flag = True
                        user_home_dir = os.path.join(home_dir,user_and_passwd[0])
                        if not os.path.isdir(user_home_dir):
                            os.makedirs(user_home_dir)
                        os.chdir(user_home_dir)

                        #change the dir to user home...

                else:
                    self.request.send("response|201|n/a|n/a".encode())


            elif recv_list[0] == "comm":
                if login_flag:
                    command_list = recv_list[1].split(",")
                    if command_list[0] == "exit":
                        break  #退出
                    response_code = self.comm_parser(command_obj, command_list)
                    send_data = "response|%s|n/a|n/a" % response_code
                    self.request.send(send_data.encode())

                    if hasattr(command_obj,command_list[0]):
                        func = getattr(command_obj,command_list[0])
                        func(command_list[1])
                        print(command_obj,command_list)



    def comm_parser(self,command_obj, command_list):
        print(os.getcwd(),command_list)
        # if not hasattr(command_obj,command_list[0]):
        #     return 202 #'202': "FTP Command does not exist",

        if os.path.isfile(command_list[1]):
            return 204 #'204': "File is existed",

        elif os.path.isfile(command_list[1]):
            return 205 #'205': "directory is existed",

        elif command_list[1] == "n/a":
            return 206 #'206': "There is no args behind the ftp command",

        # elif not os.path.isfile(command_list[1]) and not os.path.isdir(command_list[1]):
        #     return 203 #'203': "File or directory doesn't exist",

        else:
            return 203  #'203': "File or directory doesn't exist",




config = configparser.ConfigParser()
config.read(config_file)

HOST = config["host"]["host"]
PORT = int(config["host"]["port"])

ftpserver = socketserver.TCPServer((HOST,PORT),FtpRequestHandler)
ftpserver.serve_forever()
