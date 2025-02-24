from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# Get database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@postgres:5432/mydatabase")

def connect_db():
    """Connects to PostgreSQL database and returns a cursor."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

@app.route("/")
def home():
    return jsonify({"message": "Flask API is running!"})

@app.route("/db")
def test_db():
    """Checks if the database connection works."""
    conn = connect_db()
    if conn:
        return jsonify({"status": "Connected to database!"})
    else:
        return jsonify({"status": "Database connection failed"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
