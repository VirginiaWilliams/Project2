import sqlite3

# create/connect to database
con = sqlite3.connect("testdb.db")
cur = con.cursor()
cur.execute("CREATE TABLE testTable(topic, time, color)")

cur.execute("""
    INSERT INTO testTable VALUES
        ('A', 0, 'blue'),
        ('B', 0, 'red'),
        ('C', 0, 'green'),
        ('D', 0, 'yellow'),
        ('E', 0, 'purple'),
        ('F', 0, 'orange')
""")

con.commit()

res = cur.execute("SELECT topic FROM testTable")
print(res.fetchall())
