import time
import threading

def run(n):

    print('[%s]------running----' % n)
    time.sleep(2)
    print('[%s]------done----' % n)

def main():
    t_start = time.time()
    t_list = []
    for i in range(5):
        t = threading.Thread(target=run,args=[i,])
        #time.sleep(1)
        t.start()
        print('running thread')

    for t in t_list:
        t.join()
    t_stop = time.time()
    print("main thread done,running time:",t_stop - t_start)


m = threading.Thread(target=main)
#m.setDaemon(True) #将主线程设置为Daemon线程,它退出时,其它子线程会同时退出,不管是否执行完任务
m.start()
#m.join(timeout=1.5)
