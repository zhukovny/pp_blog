import dataclasses

from fastapi import APIRouter
from starlette.responses import JSONResponse

from backend.fake_db import fake_items

router = APIRouter()


@router.get("/")
async def get_items():
    content = [
        dataclasses.asdict(item)
        for _, item in fake_items.items()
    ]
    return JSONResponse(content)


@router.get("/{item_id}")
async def get_item(item_id: int):
    return fake_items.get(item_id)


@router.post("/")
async def add_item():
    return


@router.put("/")
async def update_item():
    return


@router.delete("/{item_id}")
async def delete_item(item_id: int):
    return fake_items.pop(item_id)
