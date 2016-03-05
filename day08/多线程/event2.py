import threading
import time

def light():
    if not event.isSet():
        event.set()
    count = 0
    while count < 20:
        if count < 7:
            print("\033[42;1m[green light on]\033[0m")
        elif count < 10:
            print("\033[43;1m[yellow light on]\033[0m")
        elif count < 17:
            if event.isSet():
                event.clear()
            print("\033[41;1m[red light on]\033[0m")

        elif count < 20:
            print("\033[43;1m[yellow light on]\033[0m")
        else:
            count = 0
            event.set()
        count += 1
        time.sleep(1)

def car(n):
    while True:
        time.sleep(1)
        if event.isSet():
            print("[%s] is running..." % n)
        else:
            print("[%s] is waiting..." % n)

if __name__ == '__main__':

    event = threading.Event()
    L = threading.Thread(target=light)
    L.start()
    for i in range(5):
        c = threading.Thread(target=car,args=(i,))
        c.start()
