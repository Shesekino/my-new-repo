import os
import sqlite3

filename = 'example.py.db'

def reset_database():
    try:
        os.remove(filename)
    except OSError:
        pass

def setup_database():
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')
    cursor.execute('INSERT INTO users (name) VALUES ("Alice")')
    cursor.execute('INSERT INTO users (name) VALUES ("Bob")')
    cursor.execute('INSERT INTO users (name) VALUES ("Cartman")')
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Vulnerable to SQL Injection
    print(f"executing query: {query}")
    cursor.execute(query)
    user = cursor.fetchall()
    conn.close()
    return user

reset_database()
setup_database()
user = get_user("1 OR 1=1")

print(user)
