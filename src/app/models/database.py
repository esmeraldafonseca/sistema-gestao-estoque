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

        #tabela fornecedores
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fornecedores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE)
        """)

        conn.commit()


def update_products_suppliers():
    product_supplier_pairs = [
        (1, 3),   # fornecedor_id=1 para o produto id=3
        (1, 4),   # fornecedor_id=1 para o produto id=4
        (2, 5),   # fornecedor_id=2 para o produto id=5
        (2, 6),
    ]

    with get_Connection() as conn:
        cursor = conn.cursor()
        cursor.executemany("""
            UPDATE produtos
            SET fornecedor_id = ?
            WHERE id = ?
        """, product_supplier_pairs)
        conn.commit()

#ADICIONA COLUNA DE FORENG KEY A TABLEA PRODUTOS
def add_fornecedor_column():
    with get_Connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            ALTER TABLE produtos 
            ADD COLUMN fornecedor_id INTEGER 
            REFERENCES fornecedores(id)
        """)
        conn.commit()