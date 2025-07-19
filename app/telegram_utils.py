import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_photo_to_telegram(image_bytes: bytes, lat: float = None, lon: float = None):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        raise ValueError("Missing Telegram credentials")

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    files = {"photo": ("photo.png", image_bytes, "image/png")}

    caption = ""
    if lat is not None and lon is not None:
        # Make it easy to copy: plain text + line break
        caption = f"\n{lat:.6f}, {lon:.6f}"

    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "caption": caption,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, files=files, data=data)
    try:
        result = response.json()
    except Exception:
        return False, {"error": "Invalid response from Telegram"}

    return result.get("ok", False), result
