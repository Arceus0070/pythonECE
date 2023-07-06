import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "msit"
    )
mysql_query = mydb.cursor()
query = "insert into customers (name, address) values (%s,%s)"
a = input("Enter Name: ")
b = input("Enter Address: ")
val = (a, b)
mysql_query.execute(query, val)
mydb.commit()
print("Record added")