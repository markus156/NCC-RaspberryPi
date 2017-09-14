#MySqlHandlerAPI
import mysql.connector as mysqlconnector



class MySql():

	@staticmethod
	def GetDataset():
		config = Konfig.get("MySql.config")
		#Gets a Dataset from the MySql


	#def InsertDataset():
		#Addes a new connected client to the Database

	#def RemoveDataset():
		#Removes a Client from the Database

	def CreateObjekt():
		#Created the MySqlObjekt
		config = Konfig.get("MySql.cofig")
		mysqlobjekt = mysqlconnector.connect(
			config[config.index("Datenbank Username: ")+1],
			config[config.index("Datenbank Passwort: ")+1],
			config[config.index("Datenbank Hostname: ")+1],
			config[config.index("Datenbank Datenbank: ")+1])

		return mysqlobjekt

	#def DestroyObjekt():
		#Destroys the objekts

class Konfig():

	@staticmethod
	def get(Filename="MySql.config"):
		#Here, the config will be grabbed
		config=[]
		file = open(Filename,'r')
		for line in file:
			daten = line.split("'")
			for inhalt in daten:
				if(len(inhalt)>1):
					config.append(inhalt)
					print("Line: %s"%(str(inhalt)))
		
		return config

if __name__ == "__main__":
	MySql.GetDataset()