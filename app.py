import os
import requests
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    response = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": msg
    })
    print(response.text)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    action = data.get("action")
    symbol = data.get("symbol")
    price = data.get("price")

    msg = f"""
📊 {action}
💰 {symbol}
📍 Precio: {price}
🕒 {datetime.now().strftime('%H:%M:%S')}
"""

    send_telegram(msg)

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)