# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : cmd_client.py
@Author     : louis
@Date       : 4/29/23 19:31 
"""
import socket
import time

_all_ip = '0.0.0.0'
_ip = '127.0.0.1'
_public_ip = '124.70.14.26'
_port = 8081

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((_all_ip, _port))
while True:
    cmd = input('Please input command >>>').strip()
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))
    # fetch the length of the header
    data_size = int(client.recv(8).decode('utf-8'))
    recv_size = 0
    data = b''
    while recv_size < data_size:
        res = client.recv(1024)
        recv_size += len(res)
        data += res
    print(data.decode('utf-8'))
    print(len(data))

# 解决粘包
