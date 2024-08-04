import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "050804",
database="sample_db"
)
try:
    if mydb is None:
        print("Database is not connected")
    else:
        print("Database is connected")
    cursor=mydb.cursor()
    cursor.execute("create table employee (id int primary key,name varchar(10),sal int)")
    print("Employee table created")
except error as e:
    print(e)