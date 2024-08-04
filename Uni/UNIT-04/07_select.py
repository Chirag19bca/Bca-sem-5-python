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
    cursor.execute("select * from employee")
    rows=cursor.fetchall()
    print(rows)
    #to display all records
    for i in rows:
        print(i)
    mydb.commit()
except error as e:
    print(e)