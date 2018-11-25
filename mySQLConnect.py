import mysql.connector 

dba = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="password", 
    database="familyGuy")
mycursor = dba.cursor()
##when insering don't forget to use .commit() or changes won't be made to the table
mycursor.execute("select name from actors")

for x in mycursor:
  print(str(x) +" - is an actor on family guy" ) 