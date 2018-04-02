# Create messages db

import sqlite3
from datetime import datetime

create_table = "CREATE TABLE messages (id INTEGER PRIMARY KEY, date text, sender text, number text, message text)"
date = str(datetime.now())
testmsg1 = [None, date, "Some other sender", "111-222-4834", "This is another test message"]
testmsg2 = [None, date, "Test Sender", "111-222-4834", "This is a test message"]
testmsg3 = [None, date, "Somebody else", "135-222-4834", "This is a test message"]




conn = sqlite3.connect('messages.db') 

with conn:
	cursor = conn.cursor()
	cursor.execute("DROP TABLE IF EXISTS messages")
	cursor.execute(create_table)
	cursor.execute("INSERT into messages VALUES(?,?,?,?,?)", testmsg1)
	cursor.execute("INSERT into messages VALUES(?,?,?,?,?)", testmsg2)
	cursor.execute("INSERT into messages VALUES(?,?,?,?,?)", testmsg3)

