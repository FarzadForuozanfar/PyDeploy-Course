from typing import Optional
from sqlalchemy.orm import Session
import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = get_user(db=db, user_id=user_id)
    if (user):
        db.delete(user)
        db.commit()
        return True
    
    return None

def update_user(db: Session, user_id: int, name: Optional[str] = None, email: Optional[str] = None):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        db.commit()
        db.refresh(user)
        return user
    return None

