from sqlalchemy.orm import Session
from .. import  schema
from fastapi import HTTPException, status
from Blog.models import model


def get_all_blog(db: Session):
    blogs = db.query(model.Blog).all()
    return blogs


def create_blog(request:schema.BlogCreate, db:Session):
    user = db.query(model.User).filter(model.User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_blog = model.Blog(title = request.title, body = request.body, user_id = request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update_blog(id: int, request: schema.UpdateBlog, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return blog



def delete_blogs(id: int, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    db.query(model.Blog).filter(model.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Message': f'The blog with id {id} is successfully deleted'}


