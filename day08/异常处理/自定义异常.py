
#自定义异常
class myexception(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

a = 1

try:
    assert a == 2  #断言,判断右边的条件,不成立就抛出异常 AssertionError
                   #比如说针对十分重要的条件,不通过就不进行下一步操作...一般不捕捉.

    #raise myexception("it is my exception")    #手动抛异常

except myexception as e:    #捕捉异常
    print("my err:",e)


else:
    print("没异常的时候,我才执行.")

finally:
    print("不管有没有异常,我都执行.")