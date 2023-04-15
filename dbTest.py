import sqlite3

# create/connect to database
con = sqlite3.connect("testdb.db")
cur = con.cursor()
cur.execute("CREATE TABLE testTable(topic, time, color)")

cur.execute("""
    INSERT INTO testTable VALUES
        ('ASL', 0, 'blue'),
        ('B', 0, 'red')
""")

con.commit()

res = cur.execute("SELECT topic FROM testTable")
print(res.fetchall())
