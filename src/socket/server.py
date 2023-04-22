# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : server.py
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

# 2. bind address
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sk.bind((_ip, _port))
sk.bind((_cip, _port))

# 3. 监听请求
sk.listen(5)    # 半连接池大小
print('服务端启动成功，在', _port ,'端口等待连接...')

# 4. 取出连接请求，开始服务

# 持续提供服务，并发提供服务
conn, addr = sk.accept()
print('客户端 ip + port:', addr)

# 5. 数据传输
while True:
    try:
        data = conn.recv(1024)
    except:
        print('服务端程序正在退出中...')
        break
    if not data:
        print('服务端程序正在退出中...')
        break
    data = data.decode('utf-8')
    print('客户端发来的数据:', data)

    conn.send(data.upper().encode('utf-8'))

# 6. terminate current service
conn.close()

# optional, like close all server
# sk.close()