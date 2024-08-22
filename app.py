from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)



def create_database():
    conn = sqlite3.connect('message.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, message TEXT,username TEXT NOT NULL)''')
    conn.commit()
    conn.close()



@app.route('/')
def index():
    conn = sqlite3.connect('message.db')
    c = conn.cursor()
    c.execute('SELECT * FROM messages')
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/read')
def read():
    conn = sqlite3.connect('message.db')
    c = conn.cursor()
    c.execute('SELECT * FROM messages')
    messages = c.fetchall()
    conn.close()
    return render_template('read.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_task():
    message = request.form['message']
    username = request.form['username']
    conn = sqlite3.connect('message.db')
    c = conn.cursor()
    c.execute('INSERT INTO messages (message, username) VALUES (?,?)', (message,username))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:message_id>')
def delete_task(message_id):
    conn = sqlite3.connect('message.db')
    c = conn.cursor()
    c.execute('DELETE FROM messages WHERE id = ?', (message_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_database()
    app.run(debug=True)

