from model import Todo

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.TodoList
collection = database.todo


async def already_exist(new_document):
    return collection.find({'UserIDS': {"$in": new_document}}).count() > 0

async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    if not already_exist(todo):
        return await collection.insert_one(todo)
    return None

async def update_todo(title, desc):
    await collection.update_one(
        {
            "title": title,
        },
        {
            "$set": {
                "description": desc,
            }
        }
    )
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title):
    await collection.delete_one({"tilte": title})
    return True


