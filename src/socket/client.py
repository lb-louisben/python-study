# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : client.py
@Author     : louis
@Date       : 4/22/23 16:12 
"""

import socket

_cip = '127.0.0.1'
_ip = '192.168.123.168'
public_ip = '124.70.14.26'
_port = 8081

# 1. create socket object
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 流式协议 - (TCP 协议), SOCK_DGRAM (数据报 UDP协议)

# 2. 建立连接
# sk.connect((public_ip, _port))
sk.connect((_cip, _port))

# 3. 传输数据
while True:
    msg = input('请输入>>> ').strip()
    sk.send(msg.encode('utf-8'))
    if not msg:
        continue
    if msg == 'q':
        print('客户端程序正在退出中...')
        break

    data = sk.recv(1024)
    print('服务端返回的数据:', data.decode('utf-8'))

# 4. terminate currennt service
sk.close()
