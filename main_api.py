from fastapi import FastAPI
from app.api.routes import router
from app.utils.async_queue import async_worker
import asyncio

app = FastAPI(title="Math Microservice API")
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    try:
        asyncio.create_task(async_worker())
    except Exception as e:
        print(f"[Startup Error] Failed to start async_worker: {e}")
