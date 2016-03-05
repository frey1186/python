import socketserver

class MyTCPserver(socketserver.BaseRequestHandler):

    def setup(self):
        print("NEW CONNECT",self.client_address)

    def handle(self):


        while True:

            data = self.request.recv(1024)
            if not data:
                break
            print("client %s %s say:" % self.client_address, data.decode())
            self.request.send(data)

    def finish(self):
        print("%s %s finished" % self.client_address)




if __name__ == '__main__':

    HOST,PORT = "127.0.0.1",55011

    server = socketserver.ThreadingTCPServer((HOST,PORT), MyTCPserver)

    server.serve_forever()