from typing import Union

from fastapi import FastAPI, Body
from pydantic import BaseModel
from database import read_users,create_user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World!!!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/users")
def get_users():
    return read_users()

@app.post("/users")
def post_user(id: int = Body(...),name: str = Body(...),role: str = Body(...),color: str = Body(...)):
    create_user(id,name,role,color)
    return 



