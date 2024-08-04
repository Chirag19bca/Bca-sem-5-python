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
    cursor.execute("create table new_employee_tbl(eno int ,ename char(30),gender char(1),salary float)")
    mydb.commit()
    print("new table created")
    
except error as e:
    print(e)