import os
import hashlib
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




class op_server(object):

    def __init__(self,conn):
        self.conn = conn

    def put(self,file_name):

        pass

    def get(self,file_name):
        if os.path.isfile(file_name):
            f = open(file_name,"rb")
            file_size = os.stat(file_name).st_size
            file_md5 = hashlib.md5()
            #发送文件类型|文件名称|文件大小
            file_head = "FILE|%s|%s" % (file_name,file_size)
            self.conn.send(file_head.encode())
            ack_msg = self.conn.recv(1024)
            if ack_msg.decode() == 'CLIENT_READY_TO_RECV':
                while True:
                    file_content = f.read(1024)
                    if not file_content:break
                    self.conn.send(file_content)
                    file_md5.update(file_content)
                file_get_ack = self.conn.recv(1024)
                if file_get_ack.decode() == "GET_FILE_DONE":
                    #开始验证文件完整性
                    self.conn.send(file_md5.hexdigest().encode())
                    f.close()
                elif file_get_ack.decode() == "GET_FILE_FAILED":
                    return 1
        else:
            file_head = "NOTFILE|"
            self.conn.send(file_head.encode())





    def ls(self):
        pass

    def cd(self):
        pass

    def lcd(self):
        pass



