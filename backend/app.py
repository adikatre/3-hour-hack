from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import sqlite3

# REGISTER BLUEPRINTS
from api.addMeds import addMeds_bp # addMeds.py

app = Flask(__name__)
CORS(app)

# --- Helper: get DB connection ---
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # makes rows behave like dicts
    return conn

# --- Initialize DB and create table if not exists ---
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS medications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            frequency INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

# Call on startup
init_db()

app.register_blueprint(addMeds_bp, url_prefix="/api")

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
