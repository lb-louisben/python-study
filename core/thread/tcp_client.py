# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : tcp_client.py
@Author     : louis
@Date       : 5/13/23 16:42 
"""

import socket

_all_ip = '0.0.0.0'
_ip = '127.0.0.1'
_public_ip = '124.70.14.26'
_port = 8081

client = socket.socket()
client.connect((_ip, _port))

while True:
    client.send(b'hello')
    data = client.recv(1024)
    print(data)