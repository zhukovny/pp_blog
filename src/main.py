import dataclasses

from fastapi import FastAPI

from src.fake_db import fake_items

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/posts/")
async def get_posts():
    return [
        dataclasses.asdict(post)
        for _, post in fake_items.items()
    ]


@app.get("/post/{post_id}")
async def get_post(post_id: int):
    return fake_items.get(post_id)
