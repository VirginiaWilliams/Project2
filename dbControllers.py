import sqlite3

con = sqlite3.connect("testdb.db")
cur = con.cursor()

def getTopicColor(topicName):
    res = cur.execute("SELECT color FROM testTable WHERE topic = ?",[topicName])
    return res.fetchall()

def getTopicTime(topicName):
    res = cur.execute("SELECT time FROM testTable WHERE topic = ?",[topicName])
    return res.fetchall()

# def addTime(topicName, addedTime):
#     res = cur.execute("SELECT time FROM testTable WHERE topic = ?",[topicName])
#     newTime = res.fetchone() + addedTime