#MPythonimports
import mysql.connector as mysqlconnector
import json
import sys

#Selfimports
#none by now

class MySql():

	@staticmethod
	def GetDataset():
		config = Konfig.get("MySql.config")
		#Gets a Dataset from the MySql

	#Work in progress
	#def InsertDataset():
		#Addes a new connected client to the Database

	#Work in progress
	#def RemoveDataset():
		#Removes a Client from the Database

	#Here, the mysql objekt gets created with the login data from the configfile
	def CreateObjekt():
		#Created the MySqlObjekt
		config = Konfig.get("MySql.cofig")
		mysqlobjekt = mysqlconnector.connect(
			config['Database']['Username'], #Username
			config['Database']['Password'],	#Password
			config['Database']['Hostname'],	#Host
			config['Database']['Database'])	#and a database are grabed from an configfile

		print(mysqlobjekt)
		return mysqlobjekt

	#def DestroyObjekt():
		#Destroys the objekts

class Konfig():

	#Here, the configfile is being read and the values are later used to connect to the database
	@staticmethod
	def get(Filename="MySql.json"):
		file = open(Filename).read()

		data = json.loads(file)
		file.close()

		#print(data) #Debugpurposes
		return data


	#If the file is not there jet, it will be created
	@staticmethod
	def write(Filename="MySql.json"):
		file = open(Filename,'w')

		jsonstr = {"Database":{"Username":'[put here]',
							"Password":'[put here]',
							"Database":'[put here]',
							"Host":'[put here]'
							}}


		file.write(json.dumps(jsonstr,indent=4,separators = (',',':')))
		file.close()


#This code is just her for debugingpurposes
#if __name__ == "__main__":
	#MySql.GetDataset()
#	Konfig.write()