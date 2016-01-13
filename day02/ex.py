__author__ = 'felo'

#
# import sys
# print(sys.argv)
#


#
# t1 = (11,22,{'k1':'v1'})
# #t1[1] = 12
# t1[2]['k1'] = 22
# print(t1)


# a = 100
# print('divmod 方法：a/7')
# print(a.__divmod__(7))
#
# print('\nabs方法：a的绝对值')
# print(abs(a))
# print(a.__abs__())
#
# print('\nadd方法：a+7')
# print(a.__add__(7))
# print(a+7)



#
#
# name = 'felo'
# print(type(name))
# print(dir(name))

#
# name = str('eric')
# result = name.__contains__('er')
# print(result)
# print('er' in name)
#
# #
# # ###python2.x
# # name = 'eric{0}'
# # name.__format__('alex')
# # print(name)
#
#
# name = 'eric'
# result = name.capitalize()    #首字母大写
# print(result)
#
# result = name.casefold()        #所有小写
# print(result)
#
# result = name.center(20, '*')   #居中显示，其余用*号填充
# print(result)
#
# result = name.endswith('x', 0, 3)   #切片判断以‘x’结尾
# print(result)
#
# result = name.startswith('e', 1, 3)     #切片判断以‘e’开头
# print(result)
#
# name = '理解'
# result = name.encode('gbk')         #编码为gbk格式,默认是utf-8
# print(result)



# name = 'a\tlex'
# result = name.expandtabs()      #将TAB转换成空格，默认8个
# print(result)
#
# result = name.find('ex')     #返回找到的位置，没找到-1
# print(result)
#
# result = name.index('ex')   #返回找到的位置，没找到返回错误
# print(result)
#
# name = 'alex {0} as {1}'
# result = name.format('sb', 'eric')      #字符串拼接
# print(result)
#
# name = 'alex {name} as {id}'
# result = name.format(name='sb', id='eric')      #字符串拼接
# print(result)
#
# ## name.is*
#
# li = ['s', 'b', 'a', 'l', 'e', 'x']
# result = '_'.join(li)       #将序列连接起来
# print(result)
#
# # name.ljust()        #居左
# # name.rjust()        #居右
# # name.lstrip()       #删除左空格
# # name.rstrip()
# # name.maketrans()    #有空试下
#
#
# name = 'alexissb'
# result = name.partition('is')       #字符串分成三个部分
# print(result)
#
#
# result = name.replace('a', 'o', 1)     #替换,第三个参数为替换的个数
# print(result)
#
# # name.rfind()
# # name.rindex()
# # name.rpartition()
#
# result = name.rsplit('i')
# print(result)
# result = name.split('i')
# print(result)
#
# # name.splitlines()       #分行
# #
# # name.swapcase()     #大小写转换
# # name.title()        #字符串所有单词的首字符大写
# # name.upper()

#
# li1 =[11, 11, 22, 33]
# li1.append(44)
# print(li1)
#
# li1.clear()
# print(li1)
#
# #li1.copy()
# #li1.count()
# #li1.extend()
# #li1.insert()
#
# li1 = [11, 11, 22, 33]
# result = li1.pop(3)      #按下标删除
# print(result)
#
# li1 = [11,11,22,33]
# li1.remove(11)    #按值删除，默认删除第一个
# print(li1)
#
# li1 = [11,11,22,33]
# li1.reverse()       #翻转
# print(li1)
#
#
# #li1.sort()
#


#
# tu = (11, 22, 34,)
# li = list(tu)
# print(tu)
# print(li)
#
# # tu.count()
# # tu.index()

#
# #dic = {'k1':'v1','k2':'v2'}
# dic = dict(k1='v1', k2='v2')
#
# new_dic = dic.fromkeys(['k1', 'k2'], 'v1000')
# print(new_dic)
#
# print(dic['k1'])
# print(dic['k2'])
# #print(dic['k3'])       #报错
# print(dic.get('k3'))
# print(dic.get('k3', 'alex'))        #'k3'不存在的时候使用'alex'
#
# dic = dict(k1='v1', k2='v2')
# dic.pop('k1')           #指定key
# print(dic)
#
# dic = dict(k1='v1', k2='v2')
# dic.popitem()       #无序的
# print(dic)
#
# dic['k3'] = 123
# dic.setdefault('k4')        #默认值None
# print(dic)
#
# dic = dict(k1='v1', k2='v2')
# dic.update({'k3':123})
# print(dic)


li1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90, ]
dic = {}

for i in li1:
    if i > 66:
        if 'k1' in dic.keys():
            dic['k1'].append(i)
        else:
            dic['k1'] = [i, ]
    else:
        if 'k2' in dic.keys():
            dic['k2'].append(i)
        else:
            dic['k2'] = [i, ]

print(dic)





name = 'Yang'
res = name.lower()
print(res)

name = {'name':0, 'age':1}
print(dir(name))






