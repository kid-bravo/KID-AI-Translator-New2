# server.py
# Compose FASTAPI API + Bot (ASGI) into a single app
from fastapi import FastAPI
from app.main import app as api_app
from bot.asgi import app as bot_app

app = FastAPI(title="api-bot-composed")

# Bot app sudah expose /api/messages (lihat bot/asgi.py di atas)
# Maka kita mount saja keduanya di root agar route tidak berubah
app.mount("/", bot_app)   # /api/messages milik bot tetap aktif
app.mount("/", api_app)   # API utama tetap hidup (healthz dsb.)
