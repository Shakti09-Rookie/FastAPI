from sqlalchemy.orm import Session
from .. import models, schemas, hashing
from fastapi import HTTPException, status


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        age=request.age,
        password=hashing.Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {id} is not available",
        )
    return user
