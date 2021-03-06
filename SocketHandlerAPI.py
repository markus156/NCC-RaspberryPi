#Pythonimports
import socket
import threading
from pydispatch import dispatcher

#Selfimports
#none by now

global ConnectedClients
ConnectedClients=[]


ThreadSignal= "Resend Clients"
ThreadSender= "Thread"

#---------------------------------------------------
#Class HandleSocketConnections
#Handels the clientconnections and recvives the data
#---------------------------------------------------
class HandleSocketConnections(threading.Thread):
	def __init__(self,clientsocket,adresse):
		threading.Thread.__init__(self)
		self.clientsocket=clientsocket
		self.adresse=adresse

	def run(self):
		#The Handler gets called with the clientsocket and the clientadresse
		HandleSocketConnections.Handler(self.clientsocket,self.adresse)
	
	@staticmethod
	def Handler(clientsocket,adresse):
		while True:
				#The recived data gets stored in the varable data, the maximum lenth is 1024 characters
				daten = clientsocket.recv(1024)
				#If the Lenth is 1 or under, the client has disconnected
				if (len(daten)>1 & self.CurrentStatus):
					PrintHandler = Printhandler(daten)
					PrintHandler.start()
				else:
					#If the < than 1, than the client has disconnected and we can close the thread
					#because ist is not longer needed
					print("Client %s disconnected"%(str(adresse)))
					ConnectedClients.remove(adresse)
					#conClients.remove(str(adresse))
					break


#------------------------------------------------------------------------------------
#Waits for incomming conenctions and than starts a new HandleSocketConnection-Thread
#------------------------------------------------------------------------------------
class WaitOnConnection(threading.Thread):
	def __init__(self,sock):
		threading.Thread.__init__(self)
		self.sock = sock

	def run(self):
		WaitOnConnection.Handler(sself.sock)

	@staticmethod
	def Handler(sock):
		while True:
				#Hier bleibt er stecken!!!!!
				print("Started an handlerthread")
				try:
					clientsocket,adresse = sock.accept()
				except KeyboardInterrupt:
					print("KeyBoardInterrupt")
				print("Client %s connected to the NCC"%(str(adresse)))
				ConnectedClients.append(adresse)
				#conClients.append(str(adresse))
				#If a client connects, an new thread gets created and the data is 
				#being processed in this new thread
				Clienthandler = HandleSocketConnections(clientsocket,adresse)
				Clienthandler.start()

class Printhandler(threading.Thread):
	def __init__(self,text):
		threading.Thread.__init__(self)
		self.text=text

	def run(self):
		print(self.text)

def getConnected():
	return ConnectedClients

