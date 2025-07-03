import sqlite3


def create_table_users():
    conn = sqlite3.connect('ansar.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            telegram_id INTEGER UNIQUE,
            first_name TEXT,
            age INTEGER
        )
    ''')
    conn.commit()
    conn.close()