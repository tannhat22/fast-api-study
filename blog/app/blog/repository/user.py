from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from ..hashing import Hash
from .. import schemas, models

def create_user(db: Session, user: schemas.User):
    newUser = models.User(name=user.name, email=user.email, password=Hash.bcrypt(user.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def get_user(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} not found")
    return user