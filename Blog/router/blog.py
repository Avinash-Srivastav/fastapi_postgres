
from fastapi import APIRouter , status, Depends,  HTTPException
from .. import schema, database
from sqlalchemy.orm  import Session
from .. respoite import blog
from ..auth2 import get_current_user
from Blog.models import model


router = APIRouter(
    prefix="/blogs",
    tags=['blogs']
)
get_db = database.get_db

@router.get('/', status_code=status.HTTP_200_OK)
def fetch_blog(db : Session = Depends(database.get_db),current_user: schema.ShowUser = Depends(get_current_user)):
    return blog.get_all_blog(db)
    

@router.get('/{id}', status_code=status.HTTP_200_OK)
def filter_blog(id: int, db: Session = Depends(database.get_db)):
    blog_item = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    return blog_item


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request :schema.Blog, db : Session = Depends(get_db), current_user: schema.ShowUser = Depends(get_current_user)):
     return blog.create_blog(request, db)    



@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED,)
def update_blog(id: int, request: schema.Blog, db: Session = Depends(get_db), current_user: schema.ShowUser = Depends(get_current_user)):
    updated_blog = blog.update_blog(id, request, db)
    return updated_blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: schema.ShowUser = Depends(get_current_user)):
    blog.delete_blogs(id, db)
    return {"detail": "Blog deleted"}

# def delete_blog(id:int, db: Session = Depends(get_db)) , current_user

