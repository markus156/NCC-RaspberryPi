import socket
import sys
import time
from threading import Thread



gotData = []

#Here, dte connected Clients get saved
conClients = []

#*********************************************************************************************************
#
#*********************************************************************************************************
class sockets():
		#*************************************************************************************************
		#This funktion only has debugpurposes
		#*************************************************************************************************
		@staticmethod
		def ToPrint(Daten):
			print(str(Daten))

		#*************************************************************************************************
		#This Funktion handels the Clientconnections and recieves the data
		#*************************************************************************************************
		@staticmethod
		def HandleClientConnection(clientsocket,adresse):
			while True:
				daten = clientsocket.recv(1024)
				if (len(daten)>1):
					Printhandler = Thread(target = sockets.ToPrint(daten))
					Printhandler.start()
				else:
					print("Client %s disconnected"%(str(adresse)))
					conClients.remove(str(adresse))
					break

		#*************************************************************************************************
		#This thread manages the Connections 
		#*************************************************************************************************
		@staticmethod
		def WaitOnConnection(socket):
			while True:
				clientsocket,adresse = socket.accept()
				print("Client %s connected to the NCC"%(str(adresse)))
				conClients.append(str(adresse))
				Clienthandler = Thread(target = sockets.HandleClientConnection(clientsocket,adresse))
				Clienthandler.start()

#********************************************************************************************************
#Here, the socketobjekt gets created
#********************************************************************************************************
def createSocket():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind(('127.0.0.1',80))
#	sock.bind((socket.gethostname(),80))

	sock.listen(5)
	return sock

def main():
	sock = createSocket()
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # damit man den Socketerroe 98 nicht bekommt

	WaitForConnection = Thread(target = sockets.WaitOnConnection(sock._sock))
	WaitForConnection.start()

	while True:
		for x in conClients:
			print(str(x))

		time.sleep(10)

if __name__ == "__main__":
	main()
