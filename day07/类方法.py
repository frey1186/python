class Animal(object):
    c_name = 100
    leg = None
    def __init__(self,name):
        self.name = name

    # @classmethod
    # def eat(self): #使用self来调用类变量
    #     print("%s is eating..." % self.c_name)
    #     print("%s is eating..." % self.name)


    @staticmethod
    def sleep():
        print("staticmethod ...")
        #print("%s is eating..." % self.c_name)
        #print("%s is eating..." % self.name)

    @property
    def leg_count(self):  #需要返回值
        return self.leg

    @leg_count.setter
    def leg_count(self,num):
        self.leg = num
        return self.leg

    @leg_count.deleter
    def leg_count(self):
        del self.leg



a = Animal("Dog")
print(a.leg_count)
Animal.leg = 2
a.leg_count = 4
print(a.leg_count)

