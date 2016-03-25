import os
import hashlib
import subprocess

class FtpCommandHandler(object):
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
        '301': "Client is ready  ",
        '302': "ftp server is ready....",
        '303': "Client ready to receive file data",
        '304': "Client get file done.",
        '305': "Server get file done.",
        '306': "Server check file md5 done.",
        '307': "Server check file md5 failed.",



    }

    def __get_response_code(self,response):
        response_list = response.split("|")
        if response_list[0] == "response":
            code = response_list[1]
            return  code

    def get(self,file_name):
        ready_recv = self.sock.recv(1024).decode()
        code = self.__get_response_code(ready_recv)
        if code == "301":
            f = open(file_name,"rb")
            file_size = os.stat(file_name).st_size
            file_md5 = hashlib.md5()
            #发送文件类型|文件名称|文件大小
            file_head = "file|%s|%s|n/a" % (file_name,file_size)
            self.sock.send(file_head.encode())
            ack_msg = self.sock.recv(1024).decode()
            if self.__get_response_code(ack_msg) == '303':
                while True:
                    file_content = f.read(1024)
                    if not file_content:break
                    self.sock.send(file_content)
                    file_md5.update(file_content)
                file_get_ack = self.sock.recv(1024).decode()
                if self.__get_response_code(file_get_ack) == "304":
                    #开始验证文件完整性
                    self.sock.send(file_md5.hexdigest().encode())
                    f.close()

    def put(self,file_name):

        file_head = self.sock.recv(1024).decode().split("|")
        if file_head[0] == "file":
            self.sock.send("response|302|n/a|n/a".encode())
            f = open(file_name,"wb")
            file_size = 0
            file_md5 = hashlib.md5()
            while file_size < int(file_head[2]):
                file_content = self.sock.recv(1024)
                file_md5.update(file_content)
                file_size += len(file_content)
                f.write(file_content)
            f.close()
            self.sock.send("response|305|n/a|n/a".encode())

            server_file_md5 = self.sock.recv(1024).decode()
            if file_md5.hexdigest() == server_file_md5:
                self.sock.send("response|306|n/a|n/a".encode())
                f.close()
                # f = open(file_name)
                # print(f.read())
            else:
                self.sock.send("response|307|n/a|n/a".encode())
                os.remove(file_name)


    def __cmd(self, cmd, obj=""):
        client_data = self.sock.recv(1024)
        if self.__get_response_code(client_data) == "301":
            cmd = "%s %s" % (cmd, obj)
            cmd_call = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
            cmd_result = cmd_call.stdout.read()
            if len(cmd_result) == 0:
                cmd_result = b"cmd execution has no output.."
            ack_msg = bytes("CMD_RESULT_SIZE|%s" %len(cmd_result) ,"utf8")
            self.sock.send(ack_msg)
            client_ack = self.sock.recv(50).decode()
            if self.__get_response_code(client_ack) == "301":
                self.sock.send(cmd_result)

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

