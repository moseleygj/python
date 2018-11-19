import mysql.connector 

db = mysql.connector.connect(host="localhost", user="root", password="password", database="mysql", auth_plugin='mysql_native_password')
print(db)