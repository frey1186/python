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


def w(func):    #装饰器，验证表达式输入格式
    def inner(arg1):
        if list(arg1).count('(') != list(arg1).count(')'):
            print("表达式括号数量不匹配。")
        elif re.findall("/\*|\*/", arg1):
            print("表达式运算符错误，出现*/或者/*。")
        elif not re.search("^[\d\+\*-/()]+$",arg1):
            print("表达式运算符错误，出现特殊字符。")
        elif re.search("[\+\*-/]+$",arg1):
            print("表达式运算符错误，以运算符结尾。")
        else:
            return func(arg1)
    return inner


def reload_str(arg1):  #整理表达式
    arg1 = arg1.replace('++', '+')
    arg1 = arg1.replace('+-', '-')
    arg1 = arg1.replace('-+', '-')
    arg1 = arg1.replace('--', '+')
    return arg1


# num = '\d+.?\d*e?-?\d*.?\d*'
# yunsuan = {
#     '+': "-?%s\+%s" % (num, num),
#     '-': "%s-%s" % (num, num),
#     '*': "%s\*%s" % (num, num),
#     '/': "%s/%s" % (num, num)
# }
# print(yunsuan[+])

yunsuan = {
    '+': "\d+\.?\d*\+-?\d+\.?\d*",  #加法，取表达式中第一个加法
    '-': "\d+\.?\d*-\d+\.?\d*",  #减法，取表达式中第一个减法
    '*': "\d+\.?\d*\*-?\d+\.?\d*",  #乘法，取表达式中第一个乘法
    '/': "\d+\.?\d*/-?\d+\.?\d*"  #除法，取表达式中第一个除法
}

def compute_one(input_str, fuhao, suanfa):
    '''
    计算一次最左边的，加减乘除
    :param input_str: 表达式
    :param fuhao: 符号，+ - * /
    :param suanfa: 算法：上述加减乘除函数
    :return:返回替换后的表达式，否返回原表达式
    '''
    m = re.search(yunsuan[fuhao], input_str)
    if m:
        m_list = m.group().split(fuhao)
        n = [float(x) for x in m_list]
        res =re.sub(yunsuan[fuhao], str(suanfa(n[0], n[1])), input_str, count=1)  #计算结果替换匹配表达式
        return res  #返回替换后的表达式
    else:
        return input_str

@w
def compute_without_brackets(arg1):
    '''
    计算一个沒有括号的表达式
    :param arg1: 表达式
    :return:返回计算结果（字符串格式）
    '''
    while True:
        #匹配最左边的一个*或者/
        yunsuanfu = re.search("\*|/", arg1)
        if yunsuanfu:  #计算*或者/
            if yunsuanfu.group() == '*':
                arg1 = compute_one(arg1, '*', my_cheng)
            elif yunsuanfu.group() == '/':
                arg1 = compute_one(arg1, '/', my_chu)
        else:  #计算完成乘除后计算加减
            arg1 = reload_str(arg1)  #整理表达式
            yunsuanfu = re.search("\d+\.?\d*[\+\-]\d+\.?\d*", arg1)
            if yunsuanfu:  #加减不用按顺序执行，两个函数都执行即可
                arg1 = compute_one(arg1, '-', my_jian)
                arg1 = compute_one(arg1, '+', my_jia)
            else:
                return arg1

@w
def compute_with_brackets(arg1):
    '''
    计算带括号的表达式
    :param arg1: 表达式
    :return:返回计算结果
    '''
    arg1 = reload_str(arg1)  #整理表达式
    str_in_bracket = re.search("\(([0-9\+\*-/]+)\)", arg1)  #找到表达式中的第一个最里边括号
    if str_in_bracket:
        res1 = compute_without_brackets(str_in_bracket.group(1))  #计算括号里边的值
        res = re.sub("\([0-9\+\*-/]+\)", res1, arg1, count=1)  #用值替换括号
        return compute_with_brackets(res)  #递归继续执行这个有括号计算函数
    else:
        return compute_without_brackets(arg1)    #如果沒有括号，递归无括号计算函数

def compute():
    input_str = re.sub(" ", "", input('输入计算式子：'))  #删除计算式子中的空格
    #input_str = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    #input_str = re.sub(" ", "", input_str)
    res = compute_with_brackets(input_str)  #计算
    print('计算结果：', res)
    print('eval结果：',eval(input_str))      #用于比较


if __name__ == '__main__':
    compute()
