
from fastapi import FastAPI
from . import models
from .database import engine, get_db
from .router import blog, user, resigter


app = FastAPI()

# models.base.metadata.create_all(bind=engine)


app.include_router(resigter.router)
app.include_router(blog.router)
app.include_router(user.router)
# app.include_router(protected.router)  # Include the new router/







