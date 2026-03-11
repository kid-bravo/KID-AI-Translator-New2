# server.py
# Komposisi FastAPI utama + Bot ASGI (dipasang di /bot)
from fastapi import FastAPI
from app.main import app as api_app        # API utama (healthz, dll)
from bot.asgi import app as bot_app        # Aplikasi Bot (ASGI / Bot Framework)

# Judul bebas, tidak berpengaruh ke routing
app = FastAPI(title="api-bot-composed")

# PENTING:
# - Semua endpoint bot (termasuk /api/messages) akan berada di bawah prefix /bot
#   sehingga menjadi: /bot/api/messages
app.mount("/bot", bot_app)

# Endpoint API lain tetap di-root "/"
app.mount("/", api_app)

# (Opsional) Diagnostic: cek readiness bot & env — boleh dihapus kalau tidak perlu
try:
    from fastapi.responses import JSONResponse
    @app.get("/diag/bot")
    def diag_bot():
        import os
        adapter_ready = False
        bot_ready = False
        try:
            # Sesuaikan kalau di bot.asgi nama variabelnya berbeda
            from bot.asgi import adapter, bot
            adapter_ready = adapter is not None
            bot_ready = bot is not None
        except Exception:
            pass
        return JSONResponse({
            "env": {
                "MicrosoftAppId_set": bool(os.getenv("MicrosoftAppId")),
                "MicrosoftAppPassword_set": bool(os.getenv("MicrosoftAppPassword")),
                "MicrosoftAppTenantId_set": bool(os.getenv("MicrosoftAppTenantId")),
            },
            "bot": {
                "adapter_ready": adapter_ready,
                "bot_ready": bot_ready
            }
        })
except Exception:
    # Kalau fastapi.responses tidak ada, abaikan diag
    pass
