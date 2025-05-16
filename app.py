from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

items = [100,"pen","gelpen",10.50,True]

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    items = [item for item in items if item.id != item_id]
    return {"message": f"Item {item_id} deleted"}


