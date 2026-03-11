
# bot/asgi.py  (VARIAN A)
from fastapi import FastAPI
from bot.main import router as bot_router

app = FastAPI(title="SBCS Bot")
app.include_router(bot_router, prefix="/api")  # hasil akhir: /api/me
