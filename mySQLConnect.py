import mysql.connector 

dba = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="password", 
    database="mysql")
print(dba)
dba.close()