import sqlite3

def insert_to_table_users(telegram_id, first_name=None, age=None):
    conn = sqlite3.connect('ansar.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (telegram_id, first_name, age)
        VALUES (?, ?, ?)
    ''', (telegram_id, first_name, age))
    conn.commit()
    conn.close()


def get_user_by_id(telegram_id):
    conn = sqlite3.connect('ansar.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE telegram_id = ?
    ''', (telegram_id,))
    user = cursor.fetchone()
    conn.close()
    return user


def update_table_user(telegram_id,first_name, age):
    conn = sqlite3.connect('ansar.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE users
    SET first_name = ?, age = ?
    WHERE telegram_id = ?
    ''', (first_name, age, telegram_id))
    conn.commit()
    conn.close()