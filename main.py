from fastapi import FastAPI

# instance name is "app"
app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "Shakti"}}


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
def comments(id: int):
    return {"data": {"1", "2"}}
