import asyncore
import socket
import time

users = set()


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)

    def handle_close(self):
        import sys
        f = sys._getframe()
        filename = f.f_back.f_code.co_filename
        lineno = f.f_back.f_lineno
        print '%sxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx######################################' % filename
        print 'caller filename is bbbbbb', filename
        print 'caller lineno is', lineno
        print(len(users), 'len')
        print '######################################'
        self.close()
        users.remove(self)


class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print('Incoming connection from %s %s' % (repr(addr), sock))
            handler = EchoHandler(sock)
            users.add(handler)


server = EchoServer('localhost', 8080)
dead = 0
while users or not dead:
    try:
        asyncore.loop(1, 1, None, 1)
    except KeyboardInterrupt, e:
        server.close()
        dead = 1
