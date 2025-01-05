from flask import Flask, jsonify, request
import sqlite3

def create_app():
    app = Flask(__name__)

    # Create SQLite in-memory database connection
    def create_connection():
        conn = sqlite3.connect(':memory:')  # In-memory database
        conn.row_factory = sqlite3.Row  # To return results as dict-like rows
        return conn

    # Create the performance table
    def create_table(conn):
        with conn:
            conn.execute('''
                CREATE TABLE performance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_name TEXT NOT NULL,
                    evaluation TEXT NOT NULL
                )
            ''')

    # Insert performance data into the database
    def insert_performance(conn, name, evaluation):
        with conn:
            conn.execute(
                "INSERT INTO performance (employee_name, evaluation) VALUES (?, ?)",
                (name, evaluation)
            )

    # Fetch performance data from the database
    def get_performance_data(conn):
        cursor = conn.execute("SELECT * FROM performance")
        return cursor.fetchall()

    # Create the table when the app starts
    conn = create_connection()
    create_table(conn)

    # Route to get performance data
    @app.route('/performance', methods=['GET'])
    def get_performance():
        data = get_performance_data(conn)
        return jsonify([{
            "id": row[0],
            "employee_name": row[1],
            "evaluation": row[2]
        } for row in data])

    # Route to add performance data
    @app.route('/performance', methods=['POST'])
    def add_performance():
        data = request.get_json()
        name = data.get('employee_name')
        evaluation = data.get('evaluation')

        if not name or not evaluation:
            return jsonify({"error": "Invalid input"}), 400

        insert_performance(conn, name, evaluation)
        return jsonify({"message": "Performance data added successfully"}), 201

    return app
