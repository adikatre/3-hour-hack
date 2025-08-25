from flask import Flask, jsonify
from flask_cors import CORS

from db import init_db   # <-- import from db.py
from api.addMeds import addMeds_bp

app = Flask(__name__)
CORS(app)

# Initialize DB on startup
init_db()

# Register blueprints
app.register_blueprint(addMeds_bp, url_prefix="/api")

# Health check
@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
