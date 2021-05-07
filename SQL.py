import mysql.connector
from datetime import datetime
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    #port = 3306
    database='testdb'
    #auth_plugin='mysql_native_password'
        )
#conn.close()

# mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE testdb ")
#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, PERSONID int PRIMARY KEY AUTO_INCREMENT)")
#
# mycursor.execute("DESCRIBE Person")
#
# for x in mycursor:
#     print(x)
# mycursor.execute("INsert into Person (name,age) VALUES (%s, %s)", ("Ahmed", 37 ))
# db.commit()
#
# mycursor.execute("Select * from Person")
# for x in mycursor:
#     print(x)

##################################################
mycursor = db.cursor()
# mycursor.execute("Create TABLE Test2 (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM ('M', 'F', 'o') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")


# mycursor.execute("Insert into Test2 (name, created, gender) Values (%s,%s,%s)", ( 'Ahmed', datetime.now() ,'M' ))
# mycursor.execute("Insert into Test2 (name, created, gender) Values (%s,%s,%s)", ( 'Mohamed', datetime.now() ,'M' ))
# mycursor.execute("Insert into Test2 (name, created, gender) Values (%s,%s,%s)", ( 'Soso', datetime.now() ,'F' ))
# db.commit()

# mycursor.execute("Select * from Test2 where gender ='M' order by ID deSC ")   # ASC
# mycursor.execute("Select id, name from Test2 where gender ='M' order by ID deSC ")   # ASC?

# Alter table is used to Add, Drop and Change attributes
# mycursor.execute("Alter Table test2 add column food varchar(50) not null")   # Add Column with Food name
# mycursor.execute("Alter Table test2 drop food")  # Drop the column with food name
# mycursor.execute("Describe Test2")
# mycursor.execute("Alter table test2 change name full_name Varchar(50)")
# print(mycursor.fetchone())

mycursor.execute("Describe Test2")
for x in mycursor:
    print(x)

mycursor.execute("select * from test2")
for x in mycursor:
    print(x)


mycursor.execute("show tables")
for x in mycursor:
    print(x)