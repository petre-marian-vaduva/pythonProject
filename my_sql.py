import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd = 'Cannavaro1',
    database = 'testdatabase'
)

mycursor = db.cursor()

# mycursor.execute('CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)')
mycursor.execute('INSERT INTO Person (name, age) VALUES (%s,%s)', ('Tim', 19))
db.commit()

# mycursor.execute()

