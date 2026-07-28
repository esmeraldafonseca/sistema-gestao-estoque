import sqlite3
import os

DB_NAME = "estoque.db"

def get_Connection():
    return sqlite3.Connection(DB_NAME)

def create_table():
    with get_Connection() as conn:
        cursor = conn.Cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL)
        """)

        conn.commit()