
from sqlalchemy import  Column, Integer, String, ForeignKey
from .database import base
from sqlalchemy.orm import relationship



class User(base):
    __tablename__ = 'user_information'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=500))
    email = Column(String(length=500))
    password = Column (String(length=500))   

    blogs = relationship("Blog", back_populates="user" ) #uselist=False(this is for one-to-one relation)


class Blog(base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=50), index=True)
    body = Column(String(length=255))
    user_id = Column(Integer, ForeignKey('user_information.id'))
    user = relationship("User", back_populates="blogs")

