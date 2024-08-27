
from sqlalchemy.orm import Session
from .. import schema
from fastapi import HTTPException, status
from ..hash import Hashing
from Blog.models import model


def create_user(request: schema.UserCreate, db: Session):
    hashed_password = Hashing.bcrypt(request.password)
    new_user = model.User(
        name=request.name,
        email=request.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_user(id:int,db:Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} not found")
    return user

def get_all_user(db: Session):
    user = db.query(model.User).all()
    return user

def delete_user(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    
    db.query(model.User).filter(model.User.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Message': f'The User with id {id} is successfully deleted'}