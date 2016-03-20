#_*_coding:utf-8_*_

import optparse  #导入处理参数的模块

from twisted.internet.protocol import Protocol, ClientFactory
#导入协议类中的Procotol和client工厂类

def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, Twisted version 3.0
Run it like this:

  python get-poetry-1.py port1 port2 port3 ...
"""
    parser = optparse.OptionParser(usage)

    _, addresses = parser.parse_args()  #返回需要处理的参数,address
                                        #address为多个端口的列表

    if not addresses:  #如果不存在address
        print parser.format_help()  #打印帮助
        parser.exit()   #退出

    def parse_address(addr):   #处理address
        if ':' not in addr:    #如果没有:,就说明只有端口号,那么就就给host赋值本机ip
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)  #否则就分离address,分成host和端口

        if not port.isdigit():  #且port为数字
            parser.error('Ports must be integers.')

        return host, int(port)  #返回主机名和端口

    return map(parse_address, addresses)  #使用map函数处理address列表


class PoetryProtocol(Protocol):

    poem = ''

    def dataReceived(self, data):
        self.poem += data

    def connectionLost(self, reason):
        self.poemReceived(self.poem)

    def poemReceived(self, poem):
        self.factory.poem_finished(poem)


class PoetryClientFactory(ClientFactory):

    protocol = PoetryProtocol

    def __init__(self, callback):
        self.callback = callback

    def poem_finished(self, poem):
        self.callback(poem)


def get_poetry(host, port, callback):
    """
    Download a poem from the given host and port and invoke

      callback(poem)

    when the poem is complete.
    """
    from twisted.internet import reactor
    factory = PoetryClientFactory(callback)
    reactor.connectTCP(host, port, factory)


def poetry_main():
    addresses = parse_args()

    from twisted.internet import reactor

    poems = []

    def got_poem(poem):
        poems.append(poem)
        if len(poems) == len(addresses):
            reactor.stop()

    for address in addresses:
        host, port = address
        get_poetry(host, port, got_poem)

    reactor.run()

    for poem in poems:
        print poem


if __name__ == '__main__':
    poetry_main()