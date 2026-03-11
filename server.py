# server.py
from fastapi import FastAPI
from app.main import app as api_app       # FastAPI utama (healthz, upload, jobs, dll)
from bot.asgi import app as bot_app       # Aplikasi Bot (ASGI)

app = FastAPI(title="api-bot-composed")

# Penting: mount yang lebih spesifik dulu

app = FastAPI(title="api-bot-composed")

# Bot Framework HARUS di /api
app.mount("/api", bot_app)

# API lain tetap jalan
app.mount("/", api_app

