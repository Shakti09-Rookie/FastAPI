from pydantic import BaseModel

# base model import is required for,
# or it will show error
class Blog(BaseModel):
    title: str
    body: str
