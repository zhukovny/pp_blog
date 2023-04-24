from fastapi import FastAPI

from backend.api.api import api_router
from backend.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome, stranger!"}
