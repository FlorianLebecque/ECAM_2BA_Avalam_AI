import socket
import sys
import json



class EchoClient:
	def __init__(self, msg):
		self.__msg = msg.encode()
		self.__s = socket.socket()

	def run(self, host, port):
		self . __s . connect ( (host, port) )
		self . _send ()
		self . __s . close ()

	def _send(self):
		totalsent = 0
		while totalsent < len ( self.__msg ):
			sent = self.__s. send ( self.__msg [ totalsent :])
			totalsent += sent



msg = '{"matricules": ["18040"],"port": 8080,"name": "Sara Connor"}'

 
addr = "192.168.1.205"
port = 5001

EchoClient(msg).run(addr, port)
print("ok");
