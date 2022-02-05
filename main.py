import string
from typing import Optional
from fastapi import FastAPI

# instance name is "app"
app = FastAPI()


@app.get("/blog")
def index(limit: int = 9, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f" { limit } blogs are published from the database"}
    else:
        return {"data": f"{limit} blogs are there in the data base"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


# we put id in curly-brackets,so that we can use it as a variable in path opration functoin (def abc()).
# this is called dynamic routing.
@app.get("/blog/{id}")
# passed id in function
def blog(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int, limit=10):
    return {"data": {"1", "2"}}
