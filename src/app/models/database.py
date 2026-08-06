import sqlite3
import os

DB_NAME = "estoque.db"

def get_Connection():
    conn = sqlite3.Connection(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

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

        #tabela fornecedores
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fornecedores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE)
        """)

        #tabela produtos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quatity INTEGER NOT NULL,
            fornecedor_id INTEGER NOT NULL REFERENCES fornecedores(id))
        """)



        conn.commit()

