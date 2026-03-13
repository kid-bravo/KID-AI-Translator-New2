# server.py
from fastapi import FastAPI
from app.main import app as api_app
from bot.asgi import app as bot_app

app = FastAPI(title="api-bot-composed")

# include semua router API
for route in api_app.router.routes:
    app.router.routes.append(route)

# mount bot
app.mount("/", bot_app)
