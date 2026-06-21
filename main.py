from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import os

from app.config import settings
from app.database import engine, Base
from app.routers import auth, modules, bridge, models, telemetry

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="SPES v5.8.0 API",
    description="Synthetic Personality and Emotional System",
    version="5.8.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(modules.router, prefix="/api/modules", tags=["Modules"])
app.include_router(bridge.router, prefix="/api/bridge", tags=["Bridge"])
app.include_router(models.router, prefix="/api/models", tags=["Models"])
app.include_router(telemetry.router, prefix="/api/telemetry", tags=["Telemetry"])

@app.get("/health")
async def health():
    return {"status": "healthy", "version": "5.8.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
