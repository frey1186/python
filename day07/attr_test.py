import sys
class WebServer(object):
    def __init__(self,name,host):
        self.name = name
        self.host = host

    def start(self):
        print("server is starting...")

    def stop(self):
        print("server is stoping...")

    def restart(self):
        self.stop()
        self.start()

def run(name):
    print("%s is running..." % name)

if __name__ == '__main__':
    server = WebServer("server","localhost")
    server2 = WebServer("server2","backupserver")

    #判断属性和获取属性
    if hasattr(server,sys.argv[1]):
        func = getattr(server,sys.argv[1])
        func()

    #修改属性
    setattr(server,"s_run",run)
    server.s_run("hhha")

    #删除属性
    delattr(server,"s_run")
    #server.s_run("hhha")  #删除方法

    #删除属性
    print(server.name)
    delattr(server,"name")
    #print(server.name)    #删除变量







