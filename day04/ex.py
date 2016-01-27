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
i = '500-(500*2)'
i = re.sub('\(500\*2\)','10000',i)
print(i)

a = '9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14'
print(eval(a))

arg1 = '9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14'
yunsuanfu = re.search("\*|/", arg1)
yunsuanfu = re.search("\+|-", arg1)
print(yunsuanfu.group())

a = '2*-2.123'
b = a.split('*')
print(b)
n = [float(x) for x in b]
print(n)
p = str(n[0] * n[1])
print(p)