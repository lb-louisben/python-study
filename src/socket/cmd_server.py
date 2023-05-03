# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : cmd_server.py.py
@Author     : louis
@Date       : 4/29/23 19:38 
"""

import socket
import subprocess

_all_ip = '0.0.0.0'
_ip = '127.0.0.1'
_public_ip = '124.70.14.26'
_port = 8081

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
server.bind((_ip, _port))
server.listen(5)

while True:
    conn, addr = server.accept()
    while True:
        try:
            cmd = conn.recv(1024)
        except:
            break
        if not cmd:
            break

        # execute the command line
        obj = subprocess.Popen(
            cmd.decode('utf-8'),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout_read = obj.stdout.read()
        stderr_read = obj.stderr.read()

        data_size = len(stdout_read)+len(stderr_read)
        # 固定 header 长度为 8 字节
        header = bytes(str(data_size).encode('utf-8')).zfill(8)
        conn.send(header)
        # data
        conn.send(stdout_read)
        conn.send(stderr_read)

    conn.close()