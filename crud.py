from datetime import datetime
from db_create import cur, con

def add_task(word, level):
  current_time = datetime.now()

  cur.execute(f"INSERT INTO default_cards VALUES('{word}', '{level}', '{current_time}', 'first');")
  # (word, level, time TIME, status)
  con.commit()

def get_words():
  cur.execute("SELECT * FROM default_cards")
  print(cur.fetchall())
