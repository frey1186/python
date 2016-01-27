__author__ = 'felo'

import re

def my_jia(arg1, arg2):  #加法
    return arg1 + arg2

def my_jian(arg1, arg2):  #减法
    return arg1 - arg2

def my_cheng(arg1, arg2):  #乘法
    return arg1 * arg2

def my_chu(arg1, arg2):  #除法
    return '%.20f' % (arg1 / arg2)

# num = '\d+.?\d*e?-?\d*.?\d*'
# yunsuan = {
#     '+': "-?%s\+%s" % (num, num),
#     '-': "%s-%s" % (num, num),
#     '*': "%s\*%s" % (num, num),
#     '/': "%s/%s" % (num, num)
# }
# print(yunsuan[+])

yunsuan = {
    '+': "-?\d+\.?\d*\+-?\d+\.?\d*",
    '-': "\d+\.?\d*-\d+\.?\d*",
    '*': "\d+\.?\d*\*-?\d+\.?\d*",
    '/': "\d+\.?\d*/-?\d+\.?\d*"
}


def compute_one(input_str, fuhao, suanfa):
    #计算一次
    m = re.search(yunsuan[fuhao], input_str)
    if m:
        m_list = m.group().split(fuhao)
        n = [float(x) for x in m_list]
        res =re.sub(yunsuan[fuhao], str(suanfa(n[0], n[1])), input_str, count=1)
        return res
    else:
        return input_str


def compute_without_brackets(arg1):
    while True:
        yunsuanfu = re.search("\*|/", arg1)
        if yunsuanfu:
            if yunsuanfu.group() == '*':
                arg1 = compute_one(arg1, '*', my_cheng)
            elif yunsuanfu.group() == '/':
                arg1 = compute_one(arg1, '/', my_chu)
        else:
            arg2 = re.sub('\+-', '-', arg1)
            arg1 = re.sub('--', '+', arg2)
            yunsuanfu = re.search("\d+\.?\d*[\+\-]\d+\.?\d*", arg1)
            if yunsuanfu:
                arg1 = compute_one(arg1, '-', my_jian)
                arg1 = compute_one(arg1, '+', my_jia)
            else:
                return arg1


def compute_with_brackets(arg1):
    arg2 = re.sub('\+-', '-', arg1)
    arg3 = re.sub('--', '+', arg2)
    str_in_bracket = re.search("\(([0-9\+\*-/]+)\)", arg3)
    if str_in_bracket:
        res1 = compute_without_brackets(str_in_bracket.group(1))
        res = re.sub("\([0-9\+\*-/]+\)", res1, arg3, count=1)
        return compute_with_brackets(res)
    else:
        return compute_without_brackets(arg3)

def compute():
    input_str = re.sub(" ", "", input('输入计算式子：'))  #删除计算式子中的空格
    #input_str = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    #input_str = re.sub(" ", "", input_str)
    res = compute_with_brackets(input_str)
    print('计算结果：', res)
    print('eval结果：',eval(input_str))


if __name__ == '__main__':
    compute()
