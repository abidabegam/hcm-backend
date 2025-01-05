# routes.py
from flask import Blueprint, request, jsonify
from app.database import insert_performance, get_performance_data

routes = Blueprint('routes', __name__)

def init_routes(app, conn):
    """Initialize routes with the app and database connection."""

    @app.route('/performance', methods=['GET'])
    def get_performance():
        data = get_performance_data(conn)
        return jsonify(data)

    @app.route('/performance', methods=['POST'])
    def add_performance():
        data = request.get_json()
        name = data.get('employee_name')
        evaluation = data.get('evaluation')

        if not name or not evaluation:
            return jsonify({"error": "Invalid input"}), 400

        insert_performance(conn, name, evaluation)
        return jsonify({"message": "Performance data added successfully"}), 201