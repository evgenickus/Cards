from datetime import datetime
from db_create import cur, con

def add_task(word, level, status=1):
  current_time = datetime.now()
  cur.execute(f"INSERT INTO default_cards VALUES('{word}', '{level}', '{current_time}', '{status}');")
  con.commit()

def get_words():
  cur.execute("SELECT * FROM default_cards")
  return cur.fetchall()

def create_default_player():
  current_time = datetime.now()
  cur.execute(f"INSERT INTO player_progress VALUES('default_user', '0', '0', '{current_time}');")
  con.commit()

def find_user(name):
  cur.execute(f"SELECT * FROM player_progress WHERE name == '{name}'")
  return cur.fetchall()

def save_progress(name, rounds, step):
  current_time = datetime.now()
  cur.execute(f"UPDATE player_progress SET round = '{rounds}', step = '{step}', time = '{current_time}' WHERE name == '{name}'")
  con.commit()

  return cur.fetchall()

if find_user("default_user") == []:
  create_default_player()
