import sqlite3

con = sqlite3.connect("base.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS default_cards(word, level, time TIME, status)")

con.commit()