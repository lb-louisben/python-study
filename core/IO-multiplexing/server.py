# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : server.py
@Author     : louis
@Date       : 5/13/23 18:23 
"""

import socket
import select

_all_ip = '0.0.0.0'
_ip = '127.0.0.1'
_public_ip = '124.70.14.26'
_port = 8081


server = socket.socket()
server.bind((_all_ip, _port))
server.listen(5)
server.setblocking(False)

input_list = [server]
while True:
    rlist, wlist, xlist = select.select(input_list, [], [])
    print(rlist)
    for i in rlist:
        if i is server:
            conn, addr = i.accept()
            input_list.append(conn)
            continue
        try:
            data = i.recv(1024)
            if not data:
                i.close()
                input_list.remove(i)
                continue
            i.send(data.upper())
        except ConnectionError:
            i.close()
            input_list.remove(i)
            continue