from flask import Blueprint, request, jsonify
from app import db, get_db_connection
import sqlite3

# Create blueprint for addMeds API
addMeds_bp = Blueprint("addMeds", __name__)

# POST /api/addMeds
@addMeds_bp.route("/addMeds", methods=["POST"])
def add_meds():
    try:
        data = request.get_json()

        if not data or "name" not in data or "frequency" not in data:
            return jsonify({"error": "Missing 'name' or 'frequency'"}), 400

        name = data["name"]
        frequency = data["frequency"]

        # Insert into DB
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO medications (name, frequency) VALUES (?, ?)",
            (name, frequency)
        )
        conn.commit()
        conn.close()

        return jsonify({
            "message": "Medication added successfully",
            "medication": {
                "name": name,
                "frequency": frequency
            }
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
