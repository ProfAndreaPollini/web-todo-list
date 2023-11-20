import sqlite3 as sq

# create data.db if not exists
conn = sq.connect('data.db')

# create cursor
c = conn.cursor()

# read and execute db.sql
with open('db.sql', 'r') as f:
    sql = f.read()
    c.executescript(sql)

# commit and close
conn.commit()
conn.close()