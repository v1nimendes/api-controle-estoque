import sqlite3

DB_NOME = 'esoque.db'

def init_db():
    conn = sqlite3.connect(DB_NOME)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                quantidade INTEGER)
    ''')
    conn.commit()
    conn.close()

def get_conexacao():
    return sqlite3.connect(DB_NOME)