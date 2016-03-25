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