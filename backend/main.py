from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Ping": "Pong"}

@app.get("/api/todo")
async def get_todo():
    return await fetch_all_todos()

@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(
        404,
        f"There is no TODO item with this title {title}"
    )

@app.put("/api/todo{id}", response_model=Todo)
async def put_todo(id, data):
    return id

@app.post("/api/todo")
async def post_todo(id, data):
    return id

@app.delete("/api/todo{id}")
async def delete_todo(id):
    return id

