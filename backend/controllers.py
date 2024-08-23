from flask import jsonify,request
from db_config import db_connect, db_disconnect


def read_task():
    conn = db_connect()
    c = conn.cursor()
    c.execute('SELECT * FROM messages')
    messages = c.fetchall()
    db_disconnect(conn)
    return jsonify({"status":"status","messages":messages})


def add_task():
    data=request.json
    message = data.get('message')
    username = data.get('username')
    conn = db_connect()
    c = conn.cursor()
    c.execute('INSERT INTO messages (message, username) VALUES (?,?)', (message,username))
    conn.commit()
    db_disconnect(conn)
    return jsonify({"status": "success", "message": "Data received"}), 200