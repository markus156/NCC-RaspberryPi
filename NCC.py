#Pythonimports
import socket
import sys
import time
from threading import Thread

#Selfimports
from MySqlHandlerAPI import MySql
import SocketHandlerAPI as SocketHandler
from pydispatch import dispatcher

ThreadSignal= "Resend Clients"
ThreadSender= "Thread"

#********************************************************************************************************
#Here, the socketobjekt gets created
#********************************************************************************************************
def createSocket(adresse):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind((adresse,80))
#	sock.bind((socket.gethostname(),80))

	sock.listen(5) 	#
	return sock

#********************************************************************************************************
#This is the Main Programloop
#********************************************************************************************************
def main():
	
	sock = createSocket("127.0.0.1")
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # damit man den Socketerroe 98 nicht bekommt

	CreateConectionHandler = SocketHandler.WaitOnConnection(sock)
	CreateConectionHandler.start()


	#This will run vorever
	while True:
		connections = SocketHandler.getConnected()

		for x in connections:
			print("Client %s: %s"%(connections.index(x),str(x)))

		time.sleep(10)

	

if __name__ == "__main__":
	
	main()