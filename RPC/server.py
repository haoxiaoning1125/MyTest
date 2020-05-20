# coding=utf-8
# server

import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 8080))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        print conn.recv(1024)
        # conn.sendall("world")
        # conn.close()
