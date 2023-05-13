# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : server.py
@Author     : louis
@Date       : 5/13/23 18:00

非阻塞 io 模型对 CPU 消耗大，而且消耗在循环上
"""

import socket

_all_ip = '0.0.0.0'
_ip = '127.0.0.1'
_public_ip = '124.70.14.26'
_port = 8081

server = socket.socket()
server.bind((_all_ip, _port))
server.listen(5)

server.setblocking(False)       # 所有网络阻塞都变成非阻塞

c_list = []
d_list = []

while True:
    try:
        conn, addr = server.accept()
        c_list.append(conn)
    except BlockingIOError:
        # print("客户端数量: ", len(c_list))
        for c in c_list:
            try:
                data = conn.recv(1024)
                if not data:
                    conn.close()
                    # c_list.remove(conn) #不可以在这里删除，会存在索引错误
                    d_list.append(conn)
                conn.send(data.upper())
            except BlockingIOError:
                pass
            except ConnectionError:
                conn.close()
                d_list.append(conn)

        for d in d_list:
            c_list.remove(d)
        d_list.clear()
