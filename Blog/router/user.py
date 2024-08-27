from fastapi import APIRouter, Depends, status
from .. import schema, database
from sqlalchemy.orm  import Session
from ..respoite import user
from ..auth2 import get_current_user


router = APIRouter(
        prefix="/user_detail",
        tags=['User']
)
get_db = database.get_db

@router.post('/')
def create_user(request:schema.UserCreate, db: Session = Depends(database.get_db)):
     return user.create_user(request,db)


@router.get('/{id}')
def get_user(id:int, db: Session = Depends(database.get_db),current_user: schema.ShowUser = Depends(get_current_user)):
     return user.show_user(id,db)

@router.get('/', status_code=status.HTTP_200_OK)
def get_all_user(db : Session = Depends(database.get_db)):
     return user.get_all_user(db)

# @router.get("/protected/user-info", tags=["protected"])
# def get_user_info(current_user: schema.ShowUser = Depends(get_current_user)):
#     return current_user


@router.delete('/', status_code=status.HTTP_301_MOVED_PERMANENTLY)
def delete_user(id: int, db: Session = Depends(get_db)):
     user.delete_user(id, db)
     return {"detail": "User deleted"}


