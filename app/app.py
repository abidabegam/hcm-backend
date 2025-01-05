from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)  # Fixed __name__

# SQLite in-memory database connection
def create_connection():
    conn = sqlite3.connect(':memory:')
    return conn

# Create the performance table
def create_table(conn):
    with conn:
        conn.execute('''
            CREATE TABLE performance (
                id INTEGER PRIMARY KEY,
                employee_name TEXT,
                evaluation TEXT
            )
        ''')

# Insert performance data
def insert_performance(conn, name, evaluation):
    with conn:
        conn.execute("INSERT INTO performance (employee_name, evaluation) VALUES (?, ?)", (name, evaluation))

# Fetch performance data
def get_performance_data(conn):
    cursor = conn.execute("SELECT * FROM performance")
    return cursor.fetchall()

# Create the table when the app starts
conn = create_connection()
create_table(conn)

# Flask Route to Fetch Performance Data
@app.route('/performance', methods=['GET'])
def get_performance():
    data = get_performance_data(conn)
    return jsonify(data)

# Flask Route to Add Performance Data
@app.route('/performance', methods=['POST'])
def add_performance():
    data = request.get_json()
    name = data.get('employee_name')
    evaluation = data.get('evaluation')
    insert_performance(conn, name, evaluation)
    return jsonify({"message": "Performance data added successfully"})

if __name__ == "__main__":  # Fixed the check
    app.run(debug=True)
