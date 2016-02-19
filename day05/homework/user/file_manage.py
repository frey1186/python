import json



#读文件,转化为python对象
def file_read(file_name):
    fr = open(file_name, "r")
    obj = json.load(fr)
    fr.close()
    return obj



#将python对象写到文件中
def file_write(obj, file_name):
    fw = open(file_name, "w")
    json.dump(obj, fw)
    fw.close()

