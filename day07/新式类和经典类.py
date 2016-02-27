class A1(object):
    n = 100
    def f1(self):
        print("f1 from A1")

class A2(object):
    n = 100
    def f1(self):
        print("f1 from A2")


class B(A1):
    n = 100
    # def f1(self):
    #     print("f1 from B")


class C(A2):
    n = 100
    def f1(self):
        print("f1 from C")


class D(B,C):
    n = 100
    # def f1(self):
    #     print("f1 from D")


d = D()

d.f1()