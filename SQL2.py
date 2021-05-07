#Foreign Keys & Relating Tables

import mysql.connector
from datetime import datetime
db= mysql.connector.connect(
    host="localhost",
    user = "root",
    password="1234",
    database='testdb'

)

users = [("Ahmed", "HHHH"),("Moh", "Pass"),("Ahm", "Ah123")]
User_scores = [(20,200),(30,300),(35,350)]

mycursor = db.cursor()
mycursor.execute("Describe users")
for x in mycursor:
    print(x)

mycursor.execute("show tables")
for x in mycursor:
    print(x)

# mycursor.execute("DROP TABLE scores")
# mycursor.execute("DROP TABLE users")
# Query1 = "create Table Users (id int Primary Key AUTO_INCREMENT, name varchar(50), password varchar(50))"
# Query2 = "Create Table Scores ( userID int primary Key, Foreign Key(userID) References users(id), game1 int Default 0, game2 int default 0)"
# mycursor.execute(Query1)
# mycursor.execute(Query2)


stmt = "INSERT INTO Users (name, password) VALUES (%s, %s)"
stmt2 ="Insert into Scores (userID, game1, game2) VALUES (%s, %s,%s)"
#
# #First way
# # cursor.executemany(stmt, users)   # but we should execute this , three times (number of rows)
#
# #Another Way to insert: we can use fo loop and also insert two table in the same times
#enumerate(iterable, start=0)
for count, user in enumerate(users):
    mycursor.execute(stmt,user)
    last_id = mycursor.lastrowid
    mycursor.execute(stmt2, (last_id,) + User_scores[count])

db.commit()
#
mycursor.execute("select * from scores")
for x in mycursor:
    print(x)

mycursor.execute("select * from users")
for x in mycursor:
    print(x)
#
#
