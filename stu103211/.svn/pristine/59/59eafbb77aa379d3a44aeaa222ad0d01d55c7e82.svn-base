import os
import sys
import socket
import hashlib
import interactcommand

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
home_dir = os.path.join(base_dir,"var","users")

class interaction(object):

    def __init__(self,sys_argv):
        self.args = sys_argv
        self.argv_parser()
        self.sock_connect()
        self.response_code = {
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
        self.handle()

    def help_msg(self):
        msg = '''
        -s ftp_server_addr    :ftp server ip address, mandatory
        -p ftp_server_port    :ftp server port , mandatory
        '''
        print(msg)
        return msg

    def instruction_msg(self):
        msg = '''
        get ftp_file        : download file from ftp server
        put local_file      : upload local file to remote
        ls                  : list files on ftp server
        cd  path            : change dir on ftp server
        lcd path            : change dir on local host
        mkdir path          : make dir on ftp server
        '''
        print(msg)
        return msg

    def argv_parser(self):

        if len(self.args) != 5:  #at least 5 args,or exit
            print(self.help_msg())
            sys.exit("lack or too munch of args...")
        elif "-s" not in self.args or "-p" not in self.args:
            print(self.help_msg())
            sys.exit("wrong ftp server or port ")
        try:
            host = self.args[self.args.index("-s") + 1]
            port = self.args[self.args.index("-p") + 1]
        except Exception:
            print(self.help_msg())
            sys.exit("wrong args...")

    def sock_connect(self):
        try:
            host = self.args[self.args.index("-s") + 1]
            port = int(self.args[self.args.index("-p") + 1])
            self.sock = socket.socket() #实例化socket
            self.sock.connect((host,port)) #连接socket服务器
        except socket.error as e:
            sys.exit("\033[31;1m%s\033[0m" %e)

    def login(self,retry_times = 3):
        retry_count = 0
        while retry_count < retry_times:
            # username = input("用户名：").strip()
            # if len(username) == 0: continue
            # password = input("密码：").strip()
            # if len(password) == 0: continue
            username = "felo"
            password = "password"

            passwd_md5 = hashlib.md5()
            passwd_md5.update(password.encode())
            send_data = "auth|%s,%s|n/a|n/a" % (username, passwd_md5.hexdigest())
            self.sock.send(send_data.encode())
            recv_data = self.sock.recv(1024)
            response_code = recv_data.decode().split("|")[1]
            if response_code == "200":
                print("auth secuss.")
                user_home_dir = os.path.join(home_dir,username)
                if not os.path.isdir(user_home_dir):
                    os.makedirs(user_home_dir)
                os.chdir(user_home_dir)
                return True

            elif response_code == "201":
                print("auth failed.")
                retry_count += 1

    def interact_begin(self):
        command = interactcommand.IntercatCommand(self.sock)
        while True:
            comm_input = input("ftp>").split()
            if not comm_input:
                continue
            if len(comm_input) > 1:
                send_data = "comm|%s,%s" % (comm_input[0], comm_input[1])
            else:
                send_data = "comm|%s,n/a" % (comm_input[0],)
                comm_input.append("n/a")

            self.sock.send(send_data.encode())


            if hasattr(command,comm_input[0]):
                func = getattr(command,comm_input[0])
                func(comm_input[1])
                #print(command,comm_input)
            elif comm_input[0] == "help":
                self.instruction_msg()
            elif comm_input[0] == "exit":
                break
            else:
                print("ftp command does not existed")
                self.instruction_msg()
    def handle(self):
        if self.login(3):
            self.interact_begin()



ftp_client = interaction(["interactions.py", "-s", "127.0.0.1","-p", "12345"])



