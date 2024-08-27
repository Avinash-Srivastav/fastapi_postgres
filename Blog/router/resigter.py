from fastapi import APIRouter, Depends, HTTPException, status
from .. import schema, database, token
from sqlalchemy.orm import Session
from ..hash import Hashing
from fastapi.security import  OAuth2PasswordRequestForm
from ..auth2 import get_current_user
from Blog.models import model


router = APIRouter(
    tags=["resigter"]
)


@router.post('/login')  
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(model.User).filter(model.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"invalid_credentials")
        
    if  not Hashing.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"incorrect_password")

    
    access_token = token.create_access_token(data={"sub": user.email})
    
    return {"access_token":access_token, "token_type":"bearer"} 