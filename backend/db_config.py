import sqlite3

def connect_database():
    conn = sqlite3.connect('message.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, message TEXT,username TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def db_connect():
    conn = sqlite3.connect('message.db')
    return conn

def db_disconnect(conn):
    conn.close()