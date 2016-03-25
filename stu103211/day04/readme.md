本项目为计算器项目，输入一个表达式能够计算出值

###Install
可在python3.x环境中执行，不适用于python2.x。
执行：
\#cd code_dir
\#./homework.py 或者：#python3 homework.py
开始选择即可，输入数字和回车进行选择。

###Credits：
编写人员：felo

###History：
v1.0  2016-1-28 11:31:14

###Manifest：
####流程图：
https://www.processon.com/diagraming/56a88385e4b04c153ea08f2b

####设计思路：

1）每次取左边的第一个最里边的括号，计算括号里边的值，替换原有表达式，递归最后形成一个沒有括号的表达式；
2）对于沒有括号的表达式：编写一个只计算最左边一个乘法或除法或者加法减法的函数，每次先计算一次乘除，循环执行，完成乘除计算后
计算加减，循环，全部完成即可。



####总共包含8个函数。
def my_jia(arg1, arg2):  #加法
def my_jian(arg1, arg2):  #减法
def my_cheng(arg1, arg2):  #乘法
def my_chu(arg1, arg2):  #除法
def w(func) #增加一个装饰器，用于验证表达式输入格式正确与否
def compute_one(input_str, fuhao, suanfa):
    '''
    计算一次最左边的，加减乘除
    :param input_str: 表达式
    :param fuhao: 符号，+ - * /
    :param suanfa: 算法：上述加减乘除函数
    :return:返回替换后的表达式，否返回原表达式
def compute_without_brackets(arg1):
    '''
    计算一个沒有括号的表达式
    :param arg1: 表达式
    :return:返回计算结果（字符串格式）
    '''
def compute_with_brackets(arg1):
    '''
    计算带括号的表达式
    :param arg1: 表达式
    :return:返回计算结果
    '''
def compute():主函数
    输入表达式
    删除空格
    返回计算值

####算例：
C:\Python34\python3.exe C:/Users/yangfl/PycharmProjects/python/day04/calc2.py
输入计算式子：1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
计算结果： 2776672.6952380957
eval结果： 2776672.6952380957


