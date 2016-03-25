import os
import sys
import time
import hashlib
import subprocess

class IntercatCommand(object):
    def __init__(self,sock):
        self.sock = sock
        self.response_code = {  #respinse|200|n/a|n/a
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

    def get(self,file_name):
        recv_data = self.sock.recv(1024).decode()
        if recv_data.split("|")[1] == "204":#'204': "File is existed",

            self.sock.send("response|301|n/a|n/a".encode())

            file_head = self.sock.recv(1024).decode().split("|")
            if file_head[0] == "file":
                self.sock.send("response|303|n/a|n/a".encode())
                f = open(file_name,"wb")
                file_size = 0
                file_md5 = hashlib.md5()
                while file_size < int(file_head[2]):
                    file_content = self.sock.recv(1024)
                    file_md5.update(file_content)
                    file_size += len(file_content)
                    f.write(file_content)

                    #显示进度条
                    precent = file_size/int(file_head[2])
                    self.__progress_bar(precent)

                f.close()
                self.sock.send("response|304|n/a|n/a".encode())

                server_file_md5 = self.sock.recv(1024).decode()
                if file_md5.hexdigest() == server_file_md5:
                    print("Done")
                    f.close()
                    # f = open(file_name)
                    # print(f.read())
                else:
                    print("Failed")
                    os.remove(file_name)
        else:
            print(self.response_code[self.__get_response_code(recv_data)])

    def __progress_bar(self, precent):
        """
        显示进度条函数，格式为【50个#号】100%
        :param precent: 输入为完成百分比
        :return: 打印出进度条
        """
        if precent ==1:
            sys.stdout.write('['+'#'*50+']100.00% --> ')
        else:
            sys.stdout.write('['+'#'*int(50*precent)+' '*int((50 - 50*precent)) +']'+
                             '%.2f'% (precent*100) +'%'+'\r')
        sys.stdout.flush()

    def __get_response_code(self,response):
        response_list = response.split("|")
        if response_list[0] == "response":
            code = response_list[1]
            return  code

    def put(self,file_name):
        recv_data = self.sock.recv(1024).decode()
        if recv_data.split("|")[1] == "204":#'204': "File is existed",
            f = open(file_name,"rb")
            file_size = os.stat(file_name).st_size
            file_md5 = hashlib.md5()
            #发送文件类型|文件名称|文件大小
            file_head = "file|%s|%s|n/a" % (file_name,file_size)
            self.sock.send(file_head.encode())
            recv_ack = self.sock.recv(1024).decode()
            file_size_buf = 0
            if self.__get_response_code(recv_ack) == "302":
                while True:
                    file_content = f.read(1024)
                    if not file_content:break
                    self.sock.send(file_content)
                    file_size_buf  += len(file_content)
                    file_md5.update(file_content)

                    #显示进度条
                    precent = file_size_buf/file_size
                    self.__progress_bar(precent)
                file_get_ack = self.sock.recv(1024).decode()
                if self.__get_response_code(file_get_ack) == "305":
                    #开始验证文件完整性
                    self.sock.send(file_md5.hexdigest().encode())
                    file_md5check_ack = self.sock.recv(1024).decode()
                    if self.__get_response_code(file_md5check_ack) == "306":
                        print("Done")
                        f.close()
                    elif self.__get_response_code(file_md5check_ack) == "307":
                        print("failed")
                        print(self.response_code["307"])
        else:
            print(self.response_code[self.__get_response_code(recv_data)])


    def __cmd(self, cmd, obj=""):

        recv_data = self.sock.recv(1024).decode()
        if recv_data.split("|")[1] != "203":
            self.sock.send("response|301|n/a|n/a".encode())
        cmd_res_msg = self.sock.recv(1024).decode()
        cmd_res_msg = str(cmd_res_msg).split("|")
        if cmd_res_msg[0] =="CMD_RESULT_SIZE":
            cmd_res_size = int(cmd_res_msg[1])
            self.sock.send("response|301|n/a|n/a".encode())
            res = ''
            received_size = 0
            while received_size < cmd_res_size:
              data = self.sock.recv(1024)
              received_size += len(data)
              res += str(data.decode())
            else:
              print(str(res))
              print('-------recv done----')


    def ls(self,name):

        if os.name == "nt":
            cmd = "dir"
        else:
            cmd = "ls"

        if name == "n/a":
            self.__cmd(cmd)
        else:
            self.__cmd(cmd, name)


    def cd(self,dir_name):
        if dir_name == "n/a":
            self.__cmd("cd")
        else:
            self.__cmd("cd", dir_name)

    def pwd(self):
        self.__cmd("pwd")

    def lcd(self,dir_name):
        pass

    def mkdir(self,dir_name):
        self.__cmd("mkdir", dir_name)
