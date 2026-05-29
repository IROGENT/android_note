import sqlite3
from datetime import datetime

DATABASE_NAME = 'notes.db'


def init_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                created_at TEXT
            )
        ''')
    connection.commit()
    connection.close()


def add_note(title, content):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
            INSERT INTO notes (title, content, created_at)
            VALUES (?, ?, ?)
        ''', (title, content, created_at))
    connection.commit()
    connection.close()


def get_all_notes():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM notes ORDER BY id DESC')
    notes = cursor.fetchall()
    connection.close()
    return notes


def delete_note(note_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    connection.commit()
    connection.close()


def update_note(note_id, title, content):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('''
            UPDATE notes 
            SET title = ?, content = ?
            WHERE id = ?
        ''', (title, content, note_id))
    connection.commit()
    connection.close()


def get_note_by_id(note_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM notes WHERE id = ?', (note_id,))
    note = cursor.fetchone()
    connection.close()
    return note

