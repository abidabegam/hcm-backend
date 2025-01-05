# database.py
import sqlite3

def create_connection():
    """Create a SQLite in-memory database connection."""
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row  # Return results as dict-like rows
    return conn

def create_table(conn):
    """Create the performance table."""
    with conn:
        conn.execute('''
            CREATE TABLE performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_name TEXT NOT NULL,
                evaluation TEXT NOT NULL
            )
        ''')