import sqlite3
import os

DB_NAME = "estoque.db"

def get_Connection():
    return sqlite3.Connection(DB_NAME)

def create_table():
    with get_Connection() as conn:
        cursor = conn.cursor()
        #tabela usuarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL)
        """)

        #tabela produtos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price TEXT NOT NULL,
            quatity INTEGER)
        """)

        conn.commit()