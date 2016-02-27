

#
# class A(object):
#
#     def __init__(self):
#         print("____init___")
#
#     def __new__(cls, *args, **kwargs):
#         print("___new___")
#
# a = A()



# class A(object):
#
#     def __init__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         print("__call__")
#
# a = A()
# a()

class A(object):
    """
    这是一个测试类
    """
    c_name = "alex"
    def __init__(self):
        self.name = "f"
        self.age = 12
        self.job = "ITer"

a = A()
print(a.__doc__)
print(a.__module__)
print(a.__class__)
print(a.__dict__)
