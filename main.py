from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.conf import config
from app.routes import health, app_data, project

app = FastAPI()
app.include_router(health.router)
app.include_router(app_data.router)
app.include_router(project.router)

origins = [
    "http://localhost",
    "http://localhost:3000/*",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000/*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get Application Settings
settings = config.get_settings()


@app.get("/")
async def root():
    return {"message": "Welcome to QS Backend!", "status": "Alive"}
