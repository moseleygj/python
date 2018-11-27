import mysql.connector 

dba = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="password", 
    database="batman")

mycursor = dba.cursor()

userInsertName=input("Please enter your name:")
userInsertRole=input("Please enter your role:")
print(userInsertName,userInsertRole)
##when insering don't forget to use .commit() or changes won't be made to the table
sql="INSERT INTO characters (name, role) VALUES (%s, %s)"
value=(userInsertName, userInsertRole)
mycursor.execute(sql, value)
dba.commit()
print("write successful")
mycursor.execute("select * from characters")
for x in mycursor:
  print(str(x) +" - is an actor on family guy" ) 

  #remove extra Bs from result