# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : tcp_server.py
@Author     : louis
@Date       : 5/13/23 16:34 
"""

import socket
from threading import Thread

_all_ip = '0.0.0.0'
_ip = '127.0.0.1'
_public_ip = '124.70.14.26'
_port = 8081

def comm(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        except:
            break
    conn.close()


def run(ip, port):
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        Thread(target=comm, args=(conn,)).start()


if __name__ == '__main__':
    run(_all_ip, _port)