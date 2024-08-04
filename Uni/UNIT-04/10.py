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
    #update salary using id
    empid=input("Enter Employee id: ")
    inc=int(input("Enter Increment Amount: "))
    sql="UPDATE employee SET sal = sal + %s WHERE id = %s"
    val=(inc, empid)
    cursor.execute(sql, val)
    mydb.commit()
    print("records updated")
except Error as e:
    print(e)
