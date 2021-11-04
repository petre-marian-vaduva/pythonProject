import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd = 'Cannavaro1',
    database = 'testdatabase'
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Testing (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# mycursor.execute('INSERT INTO Testing (name, created, gender) VALUES (%s, %s, %s)', ('Marie', datetime.now(), 'F'))


