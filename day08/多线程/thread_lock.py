import time
import threading

lock = threading.Lock()

def add_num():
    global num
    print("get num",num)
    time.sleep(1)
    lock.acquire()
    num -= 1
    lock.release()

num = 100
thread_list = []
for i in range(100):
    t = threading.Thread(target=add_num)
    t.start()
    thread_list.append(t)

for i in thread_list:
    i.join()

print("num:",num)