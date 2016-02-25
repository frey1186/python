

# import os
#
# #os.system("ls")
#
# a = os.popen("ls").read()
# print(a,type(a))



# fsrc = open("src.file", "r")  #以r打开
# fdst = open("dst.file", "w")  #以w打开
# import shutil
# shutil.copyfileobj(fsrc, fdst)


# import shutil
# shutil.copyfile("src.file", "dst.file")

# import os
# os.system("chmod 777 dst.file")
# os.system("ls -l | grep file")
#
# import shutil
# shutil.copymode("src.file", "dst.file")
#
# os.system("ls -l | grep file")



# import os
#
# print("src.file=>",os.stat("src.file"))
# print("dst.file=>",os.stat("dst.file"))
#
# import shutil
# shutil.copystat("src.file", "dst.file")
#
# print("src.file=>",os.stat("src.file"))
# print("dst.file=>",os.stat("dst.file"))



# import os
# os.system("chmod 777 dst.file")
# os.system("ls -l | grep file")
# print("src.file=>",os.stat("src.file"))
# print("dst.file=>",os.stat("dst.file"))
# import shutil
# shutil.copy2("src.file", "dst.file")
#
# os.system("ls -l | grep file")
# print("src.file=>",os.stat("src.file"))
# print("dst.file=>",os.stat("dst.file"))

# import os
# os.system("find tree_dst -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'")
# import shutil
# shutil.copytree("tree_src", "tree_dst", ignore=shutil.ignore_patterns('*.py','*.pyc'))  #排除py或者pyc文件
# os.system("find tree_dst -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'")



# import os
# os.system("find tree_dst -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'")
# import shutil
# shutil.rmtree("tree_dst")
# os.system("find tree_dst -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'")

# import os
# os.system("find tree_dst -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'")
# import shutil
# shutil.move("tree_dst", "tree_dst_new")
# os.system("find tree_dst -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'")
# os.system("find tree_dst_new -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'")


# import shutil
# shutil.make_archive("src.file","tar")
# import os
# os.system("ls -l | grep src.file")


# import shutil
# shutil.make_archive("tree_src","gztar",root_dir=".")
# import os
# os.system("ls -l | grep tree_src")


# import shutil
# shutil.make_archive("src.file","zip")
# import os
# os.system("ls -l | grep src.file")


# import zipfile
# z = zipfile.ZipFile("a.zip", "w")
# z.write("src.file")
# z.write("dst.file")
# z.close()
# import os
# os.system("ls -l | grep a.zip")

# import zipfile
# z = zipfile.ZipFile("a.zip", "r")
# z.extractall()
# z.close()
# import os
# os.system("ls -l | grep .file")


# import tarfile
# t = tarfile.open("b.tar", "w")
# t.add("src.file")
# t.add("dst.file")
# t.close()
# import os
# os.system("ls -l | grep b.tar")

# import tarfile
# t = tarfile.open("b.tar", "r")
# t.extractall()
# t.close()
# import os
# os.system("ls -l | grep .file")

# class Test(object):
#     def __init__(self, n):
#         self.n = n
# t1 = Test(1111)
# t2 = Test(2222)

# t3_dict = ["alex",12,"IT"]
#
# import shelve
# d = shelve.open("shelve_test")
# d["d1"] = t1
# d["d2"] = t2
# d["d3"] = t3_dict
# d.close()





# import shelve
# d = shelve.open("shelve_test")
# # a1 = d.get("d1")
# # #print(a1.n)
# a3 = d.get("d3")
# print(a3)
# d.close()

# class Test(object):
#     def __init__(self, n):
#         self.n = n
# t1 = Test(1111)
# t2 = Test(2222)
#
# t3_dict = ["alex",12,"IT"]
#
#
# import pickle
# f = open("pickle_test.pkl","wb")
# pickle.dump(t1, f)
# pickle.dump(t2, f)
# pickle.dump(t3_dict, f)
# f.close()



# import configparser
# config = configparser.ConfigParser()  #获取一个配置文件的实例
#
# #编写配置文件
# config["DEFAULT"] = {
#     "Server":45,
#     "Client":12,
# }
#
# #编写配置文件
# config["bitbuckit.org"] = {}
# config["bitbuckit.org"]["User"] = "yangfl"
# config["bitbuckit.org"]["Port"] = "5050"
#
# #写入文件
# with open("config.conf", "w") as f:
#     config.write(f)





