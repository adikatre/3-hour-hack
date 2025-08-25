from flask import Blueprint, request, jsonify
from db import get_db_connection   # import only from db.py

addMeds_bp = Blueprint("addMeds", __name__)


@addMeds_bp.route("/addMeds", methods=["POST"])
def add_meds():
    try:
        data = request.get_json()

        if not data or "name" not in data or "frequency" not in data:
            return jsonify({"error": "Missing 'name' or 'frequency'"}), 400

        name = data["name"]
        frequency = data["frequency"]

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

# GET /api/addMeds
# Returns all stored medications


@addMeds_bp.route("/addMeds", methods=["GET"])
def get_meds():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, frequency FROM medications")
        rows = cursor.fetchall()
        conn.close()

        meds = [
            {"id": row[0], "name": row[1], "frequency": row[2]}
            for row in rows
        ]

        return jsonify(meds), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE /api/addMeds/<id>
# Deletes a medication by ID
@addMeds_bp.route("/addMeds/<int:med_id>", methods=["DELETE"])
def delete_meds(med_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if medication exists
        cursor.execute("SELECT * FROM medications WHERE id = ?", (med_id,))
        med = cursor.fetchone()
        if not med:
            conn.close()
            return jsonify({"error": "Medication not found"}), 404

        # Delete it
        cursor.execute("DELETE FROM medications WHERE id = ?", (med_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": f"Medication with id {med_id} deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Insert code here for GET & DELETE requests. Ensure that it follows the format of the rest of the file.

    except Exception as e:
        return jsonify({"error": str(e)}), 500
