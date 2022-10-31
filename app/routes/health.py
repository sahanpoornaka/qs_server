from fastapi import APIRouter
from app.conf import config

router = APIRouter()

# Get Application Settings
settings = config.get_settings()


@router.get("/check/", tags=["health"])
async def check():
    return {
        "app_name": settings.env_settings.app_name,
        "server_env": settings.env_settings.server_env,
        "serve_ip": settings.env_settings.serve_ip,
        "serve_port": settings.env_settings.serve_port,
        "status": "Alive 🟢",
    }
