import sqlite3
from datetime import datetime

DB_NAME = "quotes.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def add_quote(text: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quotes (text) VALUES (?)", (text,))
    conn.commit()
    quote_id = cursor.lastrowid
    conn.close()
    if quote_id is None:
        raise Exception("Failed to insert quote")
    return quote_id


def get_all_quotes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, created_at FROM quotes ORDER BY created_at DESC")
    quotes = cursor.fetchall()
    conn.close()
    return [
        {
            "id": quote["id"],
            "text": quote["text"],
            "created_at": quote["created_at"]
        }
        for quote in quotes
    ]


def delete_quote(quote_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quotes WHERE id = ?", (quote_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted
