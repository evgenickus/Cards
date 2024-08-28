import sqlite3

con = sqlite3.connect("base.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS default_cards(word CHAR, level CHAR, time DATETIME, status INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS player_progress(name CHAR, round INTEGER, step INTEGER, time DATETIME)")


con.commit()