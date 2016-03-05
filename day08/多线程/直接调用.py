import threading
import time
def sayhi(num,name):
    print("hello %s %s" % (name,num))
    time.sleep(3)

if __name__ == '__main__':

    t1 = threading.Thread(target=sayhi,args=("alex",1))
    t2 = threading.Thread(target=sayhi,args=("alex",2))
    t1.start()
    t2.start()