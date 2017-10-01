import sqlite3
from main import Login

conn = sqlite3.connect('login.db')

c = conn.cursor()

c.execute("""CREATE table IF NOT EXIST user (
            username text,
            password text
    )""")
    
user1 = Login('mirkezi', 'asdasd' )

c.execute ("INSERT INTO user VALUES (:username, :password)", {'username': user1.username}{'password': user1.password})

conn.commit()

conn.close()
