# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : udp_concurrency_client.py
@Author     : louis
@Date       : 5/3/23 15:38 
"""
import socket

_all_ip = '0.0.0.0'
_ip = '127.0.0.1'
_public_ip = '124.70.14.26'
_port = 8081

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # 流式协议 - (TCP 协议), SOCK_DGRAM (数据报 UDP协议)


while True:
    msg = input('请输入>>> ').strip()
    sk.sendto(msg.encode('utf-8'), (_ip, _port))

    data, addr = sk.recvfrom(1024)
    print('服务端返回的数据:', data.decode('utf-8'))

sk.close()