import sys
import asyncio
import time
import logging
from fastapi import FastAPI, Request
from routers import system, web, files
from core.config import settings

# Настраиваем систему аудита (логи будут писаться в файл рядом с main.py)
logging.basicConfig(
    filename="openclaw_audit.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = FastAPI(
    title="OpenClaw Local API",
    description="Local API for AI Agent to control the machine",
    version="1.0.0"
)

# --- MIDDLEWARE ДЛЯ АУДИТА ---
@app.middleware("http")
async def audit_log_middleware(request: Request, call_next):
    start_time = time.time()
    # Пропускаем запрос дальше к функциям
    response = await call_next(request)
    process_time = time.time() - start_time
    
    # Записываем в лог
    log_message = f"Method: {request.method} | Path: {request.url.path} | Status: {response.status_code} | Time: {process_time:.3f}s"
    logging.info(log_message)
    
    return response
# -----------------------------

app.include_router(
    system.router, 
    prefix="/api/v1/system", 
    tags=list(("System",))
)

app.include_router(
    web.router, 
    prefix="/api/v1/web", 
    tags=list(("Web",))
)

app.include_router(
    files.router, 
    prefix="/api/v1/files", 
    tags=list(("Files",))
)

if __name__ == "__main__":
    import uvicorn
    logging.info("OpenClaw API Server Started.")
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT)