from datetime import datetime
from db_create import cur, con

def add_task(word, level, status=1):
  current_time = datetime.now()
  cur.execute(f"INSERT INTO default_cards VALUES('{word}', '{level}', '{current_time}', '{status}');")
  con.commit()

def get_words():
  cur.execute("SELECT * FROM default_cards")
  return cur.fetchall()
