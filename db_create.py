import sqlite3

con = sqlite3.connect("base.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS default_cards(word CHAR, level CHAR, time DATETIME, status INTEGER)")

con.commit()