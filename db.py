import sqlite3

conn = sqlite3.connect('login.db')

c = conn.cursor()
if TABLE user == 'none':
    c.execute("""CREATE TABLE user (
            username text,
            password text
    )""")
else:
    c.execute ("INSERT INTO user VALUES ('mirkezi', 'asdasd')")

conn.commit()

c.execute("SELECT * FROM user WHERE username = 'mirkezi'")

print(c.fetcone())

conn.commit()

conn.close()
