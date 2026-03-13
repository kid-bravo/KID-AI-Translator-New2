# server.py
from fastapi import FastAPI
from app.main import app as api_app
from bot.asgi import app as bot_app

app = FastAPI(title="api-bot-composed")

# mount lebih spesifik dulu
app.mount("/bot", bot_app)
app.mount("/", api_app)
