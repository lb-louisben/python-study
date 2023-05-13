# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : tcp_client.py
@Author     : louis
@Date       : 5/13/23 16:42 
"""

import socket
from threading import Thread, current_thread

_all_ip = '0.0.0.0'
_ip = '127.0.0.1'
_public_ip = '124.70.14.26'
_port = 8081


def n_client():
    client = socket.socket()
    client.connect((_ip, _port))

    n = 0
    while True:
        msg = f'{current_thread().name}  say  {n}'
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))
        n += 1


if __name__ == '__main__':
    for _ in range(1000):
        Thread(target=n_client).start()