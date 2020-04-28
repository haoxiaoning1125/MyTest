import asyncore
import socket


class HTTPClient(asyncore.dispatcher):

    def __init__(self, host):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, 8080))
        self.buffer = 'test test'

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print('recv:', self.recv(8192))

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        # self.buffer = self.buffer[sent:]
        import time
        time.sleep(2)


client = HTTPClient('localhost')
asyncore.loop()
