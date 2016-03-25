import os
import hashlib
class op_client(object):

    def __init__(self,conn):
        self.conn = conn


    def __md5_check(self,file_name,real_md5):
        f = open(file_name,"rb")

        file_md5 = hashlib.md5()
        while True:
            fr = f.read(1024)
            if not fr:break
            file_md5.update(fr)
        if file_md5.hexdigest() == real_md5:
            return True
        else:
            return False


    def get(self,file_name):
        """
        下载文件
        :param file_name:文件名
        :return: 返回下载文件吗，在当前目录下创建文件，并进行MD5值的验证。
        """

        file_head = self.conn.recv(1024).decode().split("|")
        if file_head[0] == "FILE":
            self.conn.send("CLIENT_READY_TO_RECV".encode())
            f = open(file_name,"wb")
            file_size = 0
            while file_size < int(file_head[2]):
                file_content = self.conn.recv(1024)
                file_size += len(file_content)
                f.write(file_content)
            f.close()
            self.conn.send("GET_FILE_DONE".encode())
            file_md5_check = self.conn.recv(1024).decode()
            if self.__md5_check(file_name,file_md5_check):
                print("传输成功。")
                f.close()
            else:
                print("文件MD5值验证失败")
                os.remove(file_name)
                return False

        elif file_head[0] == "NOTFILE":
            print("not file, please input a file...")
            return 1

    def put(self,file_name):
        pass

    def ls(self,obj_name):
        pass

    def cd(self,dir_name):
        pass

    def lcd(self,dir_name):
        pass
