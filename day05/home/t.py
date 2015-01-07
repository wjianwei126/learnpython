#!/usr/bin/evn python
#coding:utf-8

import SocketServer
from SocketServer import BaseRequestHandler
from server import *


ip=('127.0.0.1',9001)
sock = SocketServer.ThreadingTCPServer(ip,MyServer)

sock.serve_forever()



