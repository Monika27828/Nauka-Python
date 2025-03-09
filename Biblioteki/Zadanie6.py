import sqlite3

def create_table():
  connection = sqlite3.connect("baza.db")
  cursor = connection.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      age INTEGER NOT NULL
      )
  ''')
  connection.commit()
  connection.close()

def insert_user(name, age):
  connection = sqlite3.connect("baza.db")
  cursor = connection.cursor()
  cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", (name, age))
  connection.commit()
  connection.close()

def get_user(user_id):
  connection = sqlite3.connect("baza.db")
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
  user = cursor.fetchone()
  connection.close()
  return user

def update_user(user_id, name, age):
  connection = sqlite3.connect("baza.db")
  cursor = connection.cursor()
  cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
  connection.commit()
  connection.close()

def delete_user(user_id):
  connection = sqlite3.connect("baza.db")
  cursor = connection.cursor()
  cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
  connection.commit()
  connection.close()