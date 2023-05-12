# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : tcp_concurrency_server.py
@Author     : louis
@Date       : 5/3/23 15:18 
"""
import socketserver

_all_ip = '0.0.0.0'
_ip = '127.0.0.1'
_public_ip = '124.70.14.26'
_port = 8081


class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)         # self.request => conn
        print(self.client_address)  #

        # 5. 数据传输
        while True:
            try:
                data = self.request.recv(1024)
            except:
                break
            if not data:
                break
            data = data.decode('utf-8')
            print('客户端发来的数据:', data)

            self.request.send(data.upper().encode('utf-8'))

sk = socketserver.ThreadingTCPServer((_all_ip, _port), RequestHandler)
sk.serve_forever()
