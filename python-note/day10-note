#目录
[TOC]

#1.Twsited网络框架初探
Twisted是一个事件驱动的网络框架，其中包含了诸多功能，例如：网络协议、线程、数据库管理、网络操作、电子邮件等。　

本次我们只学习一些关于异步IO相关的简单使用，将来陆续扩展。

##（1）事件驱动
>“ Twisted is an event-driven networking framework ”

twisted网络框架以“事件”为中心，event 是 Twisted 运转的引擎，是发生各种动作的启动器，是牵一发而动全身的核心部件。
其中很重要的一个对象reactor：为程序运行建立必须的全局循环（event loop）
##（2）异步框架
> "Twisted is event-based, asynchronous framework"

这个“异步”功能的代表就是 defferred。
defferred 的作用类似于“多线程”，负责保障多头连接、多项任务的异步执行。

##（3）创建client的套路



##（4）创建server的套路




##（5）examples-1：echoserver and client
前面两个套路还没有总结出来，后续再补充，先来看看最简单的例子。
EchoServer:
```python
from twisted.internet import protocol  #导入协议类
from twisted.internet import reactor   #导入牛逼的全局循环reactor

class Echo(protocol.Protocol):    #定义一个继承自protocol的类
    def dataReceived(self, data):  #重构dataReceived方法
        self.transport.write(data)  #这里表示将受到的data再原封不动的发送回去。

def main():
    factory = protocol.ServerFactory()  #通过协议类创建server工厂类的一个实例
    factory.protocol = Echo   #

    reactor.listenTCP(1234,factory)   #监听TCP端口，并将自定义的工厂实例作为参数导入事件中。。。
    reactor.run()    #开始事件循环，如果没有reactor.stop()，事件将一直循环

if __name__ == '__main__':
    main()
```
EchoClient：
```python
from twisted.internet import reactor, protocol  #和server端一样导入牛逼的reactor和protocol

# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""

    def connectionMade(self):    #重构此方法，用于向服务器发送消息hello alex
        self.transport.write("hello alex!")

    def dataReceived(self, data):    #重构，接受服务器发过来的消息，
        "As soon as any data is received, write it back."
        print "Server said:", data
        self.transport.loseConnection()  #并断开连接，之后调用本类中connectionLost以及EchoFactory类中的clientConnectionLost两个方法。

    def connectionLost(self, reason):    #可能表示服务器断开连接，不确定
        print "connection lost"

class EchoFactory(protocol.ClientFactory):   #继承clientFactory工厂类，重写其中的部分方法
    protocol = EchoClient  #将类中的protocol参数进行赋值，这里是继承Protocol的一个类

    def clientConnectionFailed(self, connector, reason):  #重构clientConn..这个类，
        print "Connection failed - goodbye!"  #连接错误，就打印退出，在主机名或端口号不对的情况下会出现这个情况
        reactor.stop()

    def clientConnectionLost(self, connector, reason):  #重构clentConn...这个类
        print "Connection lost - goodbye!"   #断开连接的时候会出现，
        reactor.stop()

# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()  #实例化自定义的继承clientFactory类，
    reactor.connectTCP("localhost", 1234, f)  #连接服务器
    reactor.run()  #开始运行事件

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
```
##（6）example2：再来一个传输文件的例子

server：

```python
#_*_coding:utf-8_*_
# 目标向客户端发送文件，能够实现并发

import optparse, os  #optparse模块用来处理参数输入

from twisted.internet.protocol import ServerFactory, Protocol
#导入两个主要模块serverFactory和protocol


def parse_args():  #处理参数
    usage = """usage: %prog [options] poetry-file

This is the Fast Poetry Server, Twisted edition.
Run it like this:

  python fastpoetry.py <path-to-poetry-file>

If you are in the base directory of the twisted-intro package,
you could run it like this:

  python twisted-server-1/fastpoetry.py poetry/ecstasy.txt

to serve up John Donne's Ecstasy, which I know you want to do.
"""

    parser = optparse.OptionParser(usage)  #打印usage


    #增加一个端口的可选参数，可以不加
    help = "The port to listen on. Default to a random available port."
    parser.add_option('--port', type='int', help=help)

    #增加一个接口的可选参数，表示主机名，默认localhost
    help = "The interface to listen on. Default is localhost."
    parser.add_option('--iface', help=help, default='localhost')

    #处理执行命令的参数，就是跟在文件名后面的参数
    options, args = parser.parse_args()
    print("--arg:",options,args)

    #如果沒有输入参数，输出错误
    if len(args) != 1:
        parser.error('Provide exactly one poetry file.')

    #要传输的文件  赋值
    poetry_file = args[0]

    #检查这个文件是否存在
    if not os.path.exists(args[0]):
        parser.error('No such file: %s' % poetry_file)

    #返回可选参数和文件名称
    return options, poetry_file

#定义一个Protocol的子类。
class PoetryProtocol(Protocol):

    #重构connectionMade方法：
    def connectionMade(self):
        #发送信息
        self.transport.write(self.factory.poem)
        #关闭连接
        self.transport.loseConnection()

#自定义serverFactory子类
class PoetryFactory(ServerFactory):

    #将自定义的Protocol的子类传给prototol
    protocol = PoetryProtocol

    #传入一个poem参数
    def __init__(self, poem):
        self.poem = poem


def main():

    #处理传入参数
    options, poetry_file = parse_args()
    #读取文件
    poem = open(poetry_file).read()
    #实例化PoetryFactory，将poem传入
    factory = PoetryFactory(poem)

    #导入reactor
    from twisted.internet import reactor

    #开始监听
    port = reactor.listenTCP(options.port or 9000, factory,
                             interface=options.iface)

    print 'Serving %s on %s.' % (poetry_file, port.getHost())
    #开始执行reactor
    reactor.run()


if __name__ == '__main__':
    main()

```

client:

```python
# This is the Twisted Get Poetry Now! client, version 3.0.

# NOTE: This should not be used as the basis for production code.


import optparse  #导入参数处理模块，据官方文档python2.7之后将使用argparse

#导入Protocol, ClientFactory两个牛逼的类
from twisted.internet.protocol import Protocol, ClientFactory

#处理参数
def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, Twisted version 3.0
Run it like this:

  python get-poetry-1.py port1 port2 port3 ...
"""
    #实例化
    parser = optparse.OptionParser(usage)

    #处理参数，因为只需要一个address，前面option的参数这里不需要了，咱就直接用_代替。
    _, addresses = parser.parse_args()

    #处理address，如果不存在address，就输出错误
    if not addresses:
        print parser.format_help()
        parser.exit()

    #定义一个处理address的参数
    def parse_address(addr):
        #处理addr
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)
        #处理端口
        if not port.isdigit():
            parser.error('Ports must be integers.')
        #
        #返回主机名和端口：host，port
        return host, int(port)

    #考虑到address可能有多个，因此使用map函数分别对列表中的address进行处理
    return map(parse_address, addresses)


#自定义一个protocol的子类
class PoetryProtocol(Protocol):

    #开始接受poem
    poem = ''

    #重构datareceived方法：
    def dataReceived(self, data):
        #将收到的data和poem连接上。。。
        self.poem += data

    #重构connectionLost方法
    def connectionLost(self, reason):
        self.poemReceived(self.poem)

    #定义接受poem接受方法
    def poemReceived(self, poem):
        #poem_finished
        self.factory.poem_finished(poem)

#定义一个ClientFactory的一个子类
class PoetryClientFactory(ClientFactory):

    #将PoetryProtocol赋值给protocol
    protocol = PoetryProtocol

    def __init__(self, callback):
        #自定义一个callback参数
        self.callback = callback

    #定义poem_finished方法，调用callback参数
    def poem_finished(self, poem):
        self.callback(poem)


#定义下载poem的函数，主要输入为host，和port
def get_poetry(host, port, callback):
    """
    Download a poem from the given host and port and invoke

      callback(poem)

    when the poem is complete.
    """
    #导入牛逼的teactor
    from twisted.internet import reactor
    #实例化PoetryClientFactory，导入参数callback
    factory = PoetryClientFactory(callback)
    #监听主机和端口
    reactor.connectTCP(host, port, factory)


def poetry_main():
    #得到addresses
    addresses = parse_args()

    #导入牛逼的reactor
    from twisted.internet import reactor
    #定义poem
    poems = []
    #定义函数：接受poem
    def got_poem(poem):
        #将poem添加到poems列表
        poems.append(poem)
        #如果全部接受完成，就stop
        if len(poems) == len(addresses):
            reactor.stop()

    #循环addresses
    for address in addresses:
        host, port = address
        #
        get_poetry(host, port, got_poem)

    reactor.run()  #开始执行

    #将收到的poem都打印出来
    for poem in poems:
        print poem


if __name__ == '__main__':
    poetry_main()

```



#2.Redis数据库

##(1)安装redis
ubuntu安装：
 > apt-get install redis-server

查看启动情况：

```python

root@felo-virtual-machine:~/code# ps -ef | grep redis
redis      4447      1  0 22:27 ?        00:00:00 /usr/bin/redis-server 127.0.0.1:6379
root       4490   2989  0 22:28 pts/2    00:00:00 grep --color=auto redis

```

```python
root@felo-virtual-machine:~/code# netstat -nltp
激活Internet连接 (仅服务器)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:6379          0.0.0.0:*               LISTEN      4447/redis-server 1
tcp        0      0 127.0.1.1:53            0.0.0.0:*               LISTEN      889/dnsmasq
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      852/sshd
tcp6       0      0 :::22                   :::*                    LISTEN      852/sshd

```

##(2)安装python-redis

如果有没pip，就安装之：
```python

apt-get install python-pip

```

```python

root@felo-virtual-machine:~# pip install redis
Collecting redis
  Downloading redis-2.10.5-py2.py3-none-any.whl (60kB)
    100% |████████████████████████████████| 61kB 232kB/s
Installing collected packages: redis
Successfully installed redis-2.10.5
root@felo-virtual-machine:~# python
Python 2.7.11+ (default, Feb 22 2016, 16:38:42)
[GCC 5.3.1 20160222] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> exit()
root@felo-virtual-machine:~#


```




##(3)python-redis操作

###(a) set和get

```python

import redis
r = redis.Redis(host="127.0.0.1")
r.set("foo","bar")
print(r.get("foo"))

```

###(b) 连接池

```python
import redis
p = redis.ConnectionPool(host="127.0.0.1")
r = redis.Redis(connection_pool=p)
r.set("foo","bar")
print(r.get("foo"))
```

###(c) 操作




#3.RabbitMQ队列

##（1）rabbitMQ的安装
这里用的ubuntu，记录一下ubuntu上的安装，
```
felo@u01:~$ uname -a
Linux u01 3.13.0-24-generic #47-Ubuntu SMP Fri May 2 23:30:00 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
```
根据官方文档：http://www.rabbitmq.com/install-debian.html
使用APT repositories 比较懒的办法：
1.在/etc/apt/sources.list后面添加:
```
deb http://www.rabbitmq.com/debian/ testing main
```
2.执行下面两句
```
wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc
sudo apt-key add rabbitmq-signing-key-public.asc
```
3.apt-get update.  #这句不执行也行。
4.安装
```
sudo apt-get install rabbitmq-server
```
5.启动
```
felo@u01:~$ sudo service rabbitmq-server  start
 * Starting message broker rabbitmq-server                                                         [ OK ]
felo@u01:~$
```

6.安装pika
```python
#pip install pika
#pip3 install pika
```

##（2）rabbitmq使用
python采用pika库使用rabbitmq总结，多篇笔记和示例
http://blog.csdn.net/chenjiebin/article/details/8253433


