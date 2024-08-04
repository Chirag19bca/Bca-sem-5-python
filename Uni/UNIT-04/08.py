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
    #insert data dynamically
    while('true'):
        choice=input("Would you like to enter record: ")
        if(choice=='yes' or choice=='Yes'):
            empid=input("Enter Employee id: ")
            name=input("Enter Employee name: ")
            salary=int(input("Enter Employee salary: "))
            sql="insert into employee(id,name,sal) values(%s,%s,%s)"
            val=(empid,name,salary)
            cursor.execute(sql,val)
            mydb.commit()
            print("records inserted")
            #to display all records
            for i in rows:
                print(i)
        elif(choice=='no' or choice=='No'):
            break
        else:
            print("Wrong Input")
    
except error as e:
    print(e)