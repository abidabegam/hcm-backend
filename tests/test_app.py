import pytest
from app import create_app
from app.database import create_connection, create_table
@pytest.fixture
def client():
    app = create__app()
    conn = create_connection()  # Create an in-memory connection
    create_table(conn)  # Ensure the table exists before each test

    with app.test_client() as client:
        yield client

    conn.close()  # Close connection after the test
