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