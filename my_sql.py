import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd = 'Cannavaro1',
    database = 'testdatabase'
)

users = [('tim', 'tech'),
         ('joe', 'joe123'),
         ('sarah', 'sarah123')]

users_scores = [(45,100),
                (30,200),
                (12,422)]

mycursor = db.cursor()


Q1 = 'CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))'
Q2 = 'CREATE TABLE Scores (userID int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)'

Q3 = 'INSERT INTO Users (name, passwd) VALUES (%s, %s)'
Q4 = 'INSERT INTO Scores (userID, game1, game2) VALUES (%s, %s, %s)'

for x, user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + users_scores[x])

db.commit()

mycursor.execute('SELECT * FROM Scores')
for x in mycursor:
    print(x)

mycursor.execute('SELECT * FROM Scores')
for x in mycursor:
    print(x)









