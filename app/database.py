# app/database.py

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

def insert_performance(conn, name, evaluation):
    """Insert performance data into the database."""
    with conn:
        conn.execute(
            "INSERT INTO performance (employee_name, evaluation) VALUES (?, ?)",
            (name, evaluation)
        )

def get_performance_data(conn):
    """Fetch all performance data from the database."""
    cursor = conn.execute("SELECT * FROM performance")
    return [dict(row) for row in cursor.fetchall()]
