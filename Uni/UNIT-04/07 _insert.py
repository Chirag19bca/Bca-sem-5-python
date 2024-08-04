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
    cursor.execute("insert into employee values('01','manan','150000')")
    cursor.execute("insert into employee values('02','dhurvil','180000')")
    cursor.execute("insert into employee values('03','krish','110000')")
    cursor.execute("insert into employee values('04','chirag','210000')")
    print("Employee table data inserted")
    mydb.commit()
except error as e:
    print(e)