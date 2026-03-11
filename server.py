# server.py
# Compose FastAPI API + Bot (ASGI) into a single app
from fastapi import FastAPI
from app.main import app as api_app
from bot.asgi import app as bot_app

app = FastAPI(title="api-bot-composed")

# IMPORTANT:
# Bot Framework MUST run under /api/messages
# So we mount the BOT app under /api
app.mount("/api", bot_app)   # bot endpoint => /api/messages

# Main API still accessible at root "/"
app.mount("/", api_app)
