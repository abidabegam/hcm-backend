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