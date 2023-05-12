# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : udp_concurrency_server.py
@Author     : louis
@Date       : 5/3/23 15:36 
"""
import socketserver

_all_ip = '0.0.0.0'
_ip = '127.0.0.1'
_public_ip = '124.70.14.26'
_port = 8081


class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request[1].sendto(self.request[0].upper(), self.client_address)



sk = socketserver.ThreadingUDPServer((_all_ip, _port), RequestHandler)
sk.serve_forever()
