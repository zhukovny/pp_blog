import dataclasses

from fastapi import FastAPI

from src.fake_db import fake_items

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/items/")
async def get_items():
    return [
        dataclasses.asdict(item)
        for _, item in fake_items.items()
    ]


@app.get("/item/{item_id}")
async def get_item(item_id: int):
    return fake_items.get(item_id)


@app.post("/item/")
async def add_item():
    return


@app.put("/item/")
async def update_item():
    return


@app.delete("/item/{item_id}")
async def delete_item(item_id: int):
    return fake_items.pop(item_id)
