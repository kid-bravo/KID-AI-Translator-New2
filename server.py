from fastapi import FastAPI
from app.main import app as api_app
from bot.asgi import app as bot_app

app = FastAPI(title="api-bot-composed")

# Bot Framework HARUS memakai /api
app.mount("/api", bot_app)

# API utama tetap berjalan normal
app.mount("/", api_app)
