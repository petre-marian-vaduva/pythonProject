import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd = 'Cannavaro1',
    database = 'testdatabase'
)

users = [('tim', 'tech', '1234', 'tim@gmail.com'),
         ('joe', 'joe123', '2222', 'joe@gmail.com'),
         ('sarah', 'sarah123', 'pass123', 'sarah@gmail.com')]

users_scores = [(45,100),
                (30,200),
                (12,422)]

mycursor = db.cursor()


Q1 = 'CREATE TABLE Userss (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))'
Q2 = 'CREATE TABLE Scoress (userID int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)'

mycursor.execute('SHOW TABLES')

for x in mycursor:
    print(x)






