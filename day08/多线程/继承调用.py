import threading
import time

class MyThreading(threading.Thread):

    def __init__(self,num):
        super(MyThreading,self).__init__()
        self.num = num

    def run(self):
        print("hello",self.num)
        time.sleep(3)

t1 = MyThreading(1)
t2 = MyThreading(2)

t1.start()
t2.start()

