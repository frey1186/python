from twisted.internet import protocol
from twisted.internet import reactor



class EchoClient(protocol.Protocol):


    def connectionMade(self):
        self.transport.write("hello alex.")

    def dataReceived(self, data):
        print("server say:", data)
        self.transport.loseConnection()

    def connectionLost(self,reason):
        print("===> connection lost.")


class Echofactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("connection failed...bye")
        reactor.stop()


    def clientConnectionLost(self, connector, reason):
        print("connection lost,bye...")
        reactor.stop()



def main():
    f = Echofactory()
    reactor.connectTCP("127.0.0.1",9000,f)
    reactor.run()

if __name__ == '__main__':
    main()