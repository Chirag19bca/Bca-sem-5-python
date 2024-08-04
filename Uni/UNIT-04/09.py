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
    #delete data dynamically
    empid=input("Enter Employee id: ")
    sql="delete from employee where id=%s"
    val= (empid, )
    cursor.execute(sql,val)
    mydb.commit()
    print("record deleted")
except error as e:
    print(e)