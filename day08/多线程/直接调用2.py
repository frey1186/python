import threading
import time

def sayhi(num):
    print("hello ",num)
    time.sleep(3)

if __name__ == '__main__':

    t_list = []
    #主线程 通过threading连续创建十个线程
    for i in range(10):
        t = threading.Thread(target=sayhi,args=(i,))
        t_list.append(t)  #将对象加入列表
        t.start()
    for i in t_list:  #循环列表
        i.join()  #等待线程执行完毕

    print("----over-------")  #全部执行完后,主线程执行print
