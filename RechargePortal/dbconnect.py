import mysql.connector

def dbconnect():
	mydb = mysql.connector.connect(
		host = "localhost",
		port = 3306,
		user = "root",
		passwd = "root",
    	database = "RechargePortal"
	)
	mycursor = mydb.cursor()
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

