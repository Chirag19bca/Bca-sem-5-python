import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "050804",
)

print(mydb)

try: 
    cursor = mydb.cursor()
    cursor.execute("Create database sample_db")
    cursor.execute("show databases")
    my = cursor.fetchall()
    print("Database Created \n")
    for i in my:
        print(i)
        
except error as e:
    print(e)
    
else:
    print("database already created")