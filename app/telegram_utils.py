import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_photo_to_telegram(image_bytes: bytes):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        raise ValueError("Missing Telegram credentials")

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    files = {"photo": ("photo.png", image_bytes, "image/png")}
    data = {"chat_id": TELEGRAM_CHAT_ID}

    response = requests.post(url, files=files, data=data)
    try:
        result = response.json()
    except Exception:
        return False, {"error": "Invalid response from Telegram"}

    return result.get("ok", False), result