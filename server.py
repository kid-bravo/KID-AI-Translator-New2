from fastapi import FastAPI
from app.main import app as api_app
from bot.asgi import app as bot_app

app = FastAPI(title="api-bot-composed")

app.mount("/", api_app)
app.mount("/api/messages", bot_app)
