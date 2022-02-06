from typing import List
from .. import database, schemas, models, hashing
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..repository import user

# tags=["blogs"] <- so that all the functions
#                   appear inside blogs subgrid on the page
router = APIRouter(prefix="/user", tags=["users"])
get_db = database.get_db


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)


@router.get("/", response_model=List[schemas.ShowUser])
def all_user(db: Session = Depends(get_db)):
    userss = db.query(models.User).all()
    return userss
