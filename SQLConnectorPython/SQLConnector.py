import mysql.connector

## Create SQL Connection ##
try:
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gr0v3v!shal",
    database="pos"
  )
except mysql.connector.Error as err:
  print("ERROR OCCURED - More Details : {}".format(err))
'''
## Create Database ##
mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
'''
## SQL Select Statements ##
mycursor = mydb.cursor()
mycursor.execute("select * from users")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

