#SocketHandler
import socket
import threading

class HandleSocketConnections(threading.Thread):
	def __init__(self,clientsocket,adresse):
		threading.Thread.__init__(self)
		self.clientsocket=clientsocket
		self.adresse=adresse

	def run(self):
		HandleSocketConnections.Handler(self.clientsocket,self.adresse)
	
	@staticmethod
	def Handler(clientsocket,adresse):
		while True:
				daten = clientsocket.recv(1024)
				if (len(daten)>1):
					PrintHandler = Printhandler(daten)
					PrintHandler.start()
				else:
					print("Client %s disconnected"%(str(adresse)))
					#conClients.remove(str(adresse))
					break



class WaitOnConnection(threading.Thread):
	def __init__(self,sock):
		threading.Thread.__init__(self)
		self.sock = sock

	def run(self):
		WaitOnConnection.Handler(self.sock)

	@staticmethod
	def Handler(sock):
		while (True):
				clientsocket,adresse = sock.accept()
				print("Client %s connected to the NCC"%(str(adresse)))
				#conClients.append(str(adresse))
				Clienthandler = HandleSocketConnections(clientsocket,adresse)
				Clienthandler.start()


class Printhandler(threading.Thread):
	def __init__(self,text):
		threading.Thread.__init__(self)
		self.text=text

	def run(self):
		print(self.text)