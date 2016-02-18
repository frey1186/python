# __author__ = 'felo'
#
# a = '-1+23+12-3*1+3/13*2'
# b = list(a)
# b.remove('-')
# print(b)
# c = ''.join(b)
# print(c)
#
# d = a.lstrip('-')
# print(d)
#
#
# a = '1'
# b = float(a)
# print(b)


# import re
# a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# res = re.sub("\(([0-9\+\-\*/]+)\)", 'AAA',a,count=1)
# print(a)
# if res:
#     print(res)

import re
# i = '500-(500*2)'
# i = re.sub('\(500\*2\)','10000',i)
# print(i)
#
# a = '9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14'
# print(eval(a))
#
# arg1 = '9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14'
# yunsuanfu = re.search("\*|/", arg1)
# yunsuanfu = re.search("\+|-", arg1)
# print(yunsuanfu.group())
#
# a = '2*-2.123'
# b = a.split('*')
# print(b)
# n = [float(x) for x in b]
# print(n)
# p = str(n[0] * n[1])
# print(p)

#
# arg1 = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# arg1 = re.sub('\s','',arg1)
# print(arg1)
# a = re.search("^[\d\+\*-/()]+$",arg1)
# print(a)

#
# import time
# def consumer(name):
#     print("%s 准备吃包子啦!" %name)
#     while True:
#         baozi = yield
#         print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
#
# def producer(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     c.__next__()
#     c2.__next__()
#     print("老子开始准备做包子啦!")
#     for i in range(10):
#         time.sleep(1)
#         print("做了2个包子!")
#         c.send(i)
#         c2.send(i)
#
# producer("alex")

#
def w1(func):
    def inner():
        print("验证1")
        # 验证2
        # 验证3
        return func()
    return inner

@w1
def f1():
    print('f1')

f1()

#
#
# import calc
#
# a = calc.my_jia(1,2)
# print(a)
#

#
# def Before(request,kargs):
#     print("before")
#
# def After(request,kargs):
#     print("after")
#
#
# def Filter(before_func,after_func):
#     def outer(main_func):
#         def wrapper(request,kargs):
#
#             before_result = before_func(request,kargs)
#             if(before_result != None):
#                 return before_result;
#
#             main_result = main_func(request,kargs)
#             if(main_result != None):
#                 return main_result;
#
#             after_result = after_func(request,kargs)
#             if(after_result != None):
#                 return after_result;
#
#         return wrapper
#     return outer
#
# @Filter(Before, After)
# def Index(request,kargs):
#     print('index')
#
#
# request = "request"
# kargs = "kargs"
#
# Index(request, kargs)