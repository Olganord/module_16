from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="ID of the item")):
    return {"item_id": item_id}

@app.get("/users/{user_id}")
async def get_user(user_id: Annotated[int, Path(gt=0, title="User ID", description="The ID must be a positive integer")]):
    return {"user_id": user_id}

@app.get("/users/{username}")
async def get_user_by_username(
username: Annotated[str, Path(min_length=3, max_length=20, regex="^[a-zA-Z0-9_-]+$")]
):
    return {"username": username}
