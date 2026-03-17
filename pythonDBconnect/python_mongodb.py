# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="user",
  passwd ="password"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE gfg")
