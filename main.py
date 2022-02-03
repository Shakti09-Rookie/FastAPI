from fastapi import FastAPI

# instance name is "app"
app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "Shakti"}}


@app.get("/about")
def about():
    return {"data": "about page"}
