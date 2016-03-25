ftpuser_file = "ftpuser.pkl"

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


# class users(object):
#
#     def __init__(self,name,password,login_flag):
#         self.name = name
#         self.password = password
#         self.login_flag = login_flag
#
#
#
# user_list = []
# for i in range(10):
#     user_list.append(users("user"+str(i),"password",False))


user_dict = {
    #用户名：密码，配额1024M，登录标签
    "felo":["5f4dcc3b5aa765d61d8327deb882cf99",1024,False],
    "yang":["5f4dcc3b5aa765d61d8327deb882cf99",100,False],
}

f = file_operate(ftpuser_file)
f.file_write(user_dict)