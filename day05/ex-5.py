__author__ = 'felo'

# def login(func):  #welcome
#
#     def wrapper(*args, **kwargs):
#         print("login...")
#         return func(*args, **kwargs)
#     return wrapper
#
# @login
# def welcome(name,age=0):
#     print("welcome...", name, age)
#
# welcome("alex", 19)


#递归
#明确结束条件，一般来讲成倍递减





#
#
# if __name__ == '__main__':
#     formula = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
#     res = calc(formula)
#

#import re
# a = "192.168.1.1"
# #m = re.search("(\d{1,3}(.|)){4}", a)
# #m = re.search("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", a)
# m = re.search("(\d{1,3}.){3}\d{1,3}", a)
# print(m.group())

# import re
# str1 = "18651054604"
# m = re.search("1[345678]\d{9}",str1)
# print(m.group())

# import re
# contactInfo = 'Oldboy School, Beijing Changping Shahe: 010-8343245'
# match = re.search('([a-zA-Z ]+), ([a-zA-Z ]+): ([0-9- ]+)', contactInfo) #分组
# print(match.group())
# print(match.group(1))
# print(match.group(2))
# print(match.group(3))
# match = re.search('(?P<last>[a-zA-Z ]+), (?P<first>[a-zA-Z ]+): (?P<phone>[0-9- ]+)', contactInfo)
# print(match.group())
# print(match.group("last"))
# print(match.group("first"))
# print(match.group("phone"))

# import re
# email = "alex.li@126.com   http://www.oldboyedu.com"
# m = re.search("[0-9a-z.]{1,26}@[0-9a-z.]{1,10}.[a-z.]{1,6}",email)
# print(m.group())


#冒泡
#
data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]
#
# for j in range(1, len(data)):  #range(1,15)
#
#     for i in range(len(data)-j):  #range(15-j)
#         if data[i] > data[i+1]:
#             tmp = data[i+1]         #交换位置
#             data[i+1] = data[i]
#             data[i] = tmp
# print(data)
#
#插入排序
# def insert_sort(lists):
#   # 插入排序
#   count = len(lists)
#   for i in range(1, count):
#     key = lists[i]
#     j = i - 1
#     while j >= 0:
#       if lists[j] > key:
#         lists[j + 1] = lists[j]
#         lists[j] = key
#       j -= 1
#   return lists
# a = insert_sort(data)
# print(a)
#
# import time
#
# a = time.time()
# a = time.clock()
# a = time.ctime()
# a = time.gmtime()
# #a = time.mktime()
# a = time.localtime()
# time.sleep(1)
# a = time.strftime("%Y-%m-%d %H-%M-%S") #2016-01-30 18-22-49
# a = time.strptime("2016-01-30 18-22-49", "%Y-%m-%d %H-%M-%S")

# print(a)
#
# import  datetime
# b = datetime.time()
# print(b)
#



# import random
# check_words = ''
# for i in range(4):
#     current = random.randrange(4)
#     if check_words != i:
#         check_words += str(chr(random.randint(65, 90)))
#     else:
#         check_words += str(random.randint(0, 9))
#
# print(check_words)


# import sys
# import time
#
# for i in range(10):
#     sys.stdout.write("#")
#     sys.stdout.flush()
#     time.sleep(0.5)

# import time
# import datetime
#
# print(time.clock()) #返回处理器时间,3.3开始已废弃
# print(time.process_time()) #返回处理器时间,3.3开始已废弃
# print(time.time()) #返回当前系统时间戳
# print(time.ctime()) #输出Tue Jan 26 18:23:48 2016 ,当前系统时间
# print(time.ctime(time.time()-86640)) #将时间戳转为字符串格式
# print(time.gmtime(time.time()-86640)) #将时间戳转换成struct_time格式
# print(time.localtime(time.time()-86640)) #将时间戳转换成struct_time格式,但返回 的本地时间
# print(time.mktime(time.localtime())) #与time.localtime()功能相反,将struct_time格式转回成时间戳格式
# #time.sleep(4) #sleep
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ) #将struct_time格式转成指定的字符串格式
# print(time.strptime("2016-01-28","%Y-%m-%d") ) #将字符串格式转换成struct_time格式
#
# #datetime module
#
# print(datetime.date.today()) #输出格式 2016-01-26
# print(datetime.date.fromtimestamp(time.time()-864400) ) #2016-01-16 将时间戳转成日期格式
# current_time = datetime.datetime.now() #
# print(current_time) #输出2016-01-26 19:04:30.335935
# print(current_time.timetuple()) #返回struct_time格式
#
# #datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])
# print(current_time.replace(2014,9,12)) #输出2014-09-12 19:06:24.074900,返回当前时间,但指定的值将被替换
#
# str_to_date = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M") #将字符串转换成日期格式
# new_date = datetime.datetime.now() + datetime.timedelta(days=10) #比现在加10天
# new_date = datetime.datetime.now() + datetime.timedelta(days=-10) #比现在减10天
# new_date = datetime.datetime.now() + datetime.timedelta(hours=-10) #比现在减10小时
# new_date = datetime.datetime.now() + datetime.timedelta(seconds=120) #比现在+120s
# print(new_date)

# import random
# print(random.random())  #0-1的随机浮点数
# print(random.randint(1,2))  #1-2,包括1和2
# print(random.randrange(1,10))    #1-10，包括1不包括10


#import os


# import json
# f = open("data.txt",'w')
# dic1 = {
#     "name": "alex",
#     "age": 12,
#     "job": "ITer"
# }
#
# # res = json.dumps(dic1)
# # f.write(res)
# # 等价于
# json.dump(dic1, f)
#
# f.close()

# import json
# f = open("data.txt",'r')  #使用字符串写入或读取
# #res = json.loads(f.read())
# # 等价于
# res = json.load(f)
# f.close()
# print(res)

#
# import pickle
# f = open("data.txt",'wb')  #注意使用二进制来读写
# dic1 = {
#     "name": "alex",
#     "age": 12,
#     "job": "ITer"
# }
#
# # res = pickle.dumps(dic1)
# # f.write(res)
# # 等价于
# pickle.dump(dic1, f)
#
# f.close()
#
# import pickle
# f = open("data.txt",'rb')  #使用二进制写入或读取
# #res = pickle.loads(f.read())
# # 等价于
# res = pickle.load(f)
# f.close()
# print(res)

# def w1(func):
#     def inner():
#         print("验证1")
#         # 验证2
#         # 验证3
#         return func()
#     return inner
#
# @w1
# def f1():
#     print('f1')
#
# f1()

p = [ ]
q = [ ]
a = [['ipad', 2998, 1], ['ipad', 2998, 2], ['ipad', 2998, 2], ['ipad', 2998, 2]]
for i in a:
    p.append(i[0])
    q.append(i[2])
for j in p:
    if p.count(j) >1:
        pass


a = [1,1,1,1]
print(a.index(1))