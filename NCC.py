import socket
import sys
import time
from threading import Thread
from MySqlHandlerAPI import MySql
import SocketHandlerAPI as SocketHandler




#********************************************************************************************************
#Here, the socketobjekt gets created
#********************************************************************************************************
def createSocket():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind(('127.0.0.1',80))
#	sock.bind((socket.gethostname(),80))

	sock.listen(5)
	return sock

#********************************************************************************************************
#This is the Main Programloop
#********************************************************************************************************
def main():
	sock = createSocket()
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # damit man den Socketerroe 98 nicht bekommt

	CreateConectionHandler = SocketHandler.WaitOnConnection(sock,status)
	CreateConectionHandler.start()


	#This will run vorever
	while True:
		pass

if __name__ == "__main__":
	try:
		main()
	#MySql.GetDataset()
	except KeyboardInterrupt:
		quit()


