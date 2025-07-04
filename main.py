import os
import requests
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

@app.route("/")
def home():
    return "Bot Amazon Hunter è attivo!"

@app.route("/send")
def send():
    message = "🔥 Offerta di test da Amazon Hunter!"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)
    return "Messaggio inviato!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
