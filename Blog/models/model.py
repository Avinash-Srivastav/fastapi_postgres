from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from Blog.database import base

class User(base):
    __tablename__ = 'user_information'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=500))
    email: Mapped[str] = mapped_column(String(length=500))
    password: Mapped[str] = mapped_column(String(length=500))
    # location: Mapped[str] = mapped_column(String(length=500))
    description: Mapped[str] = mapped_column(String(length=500), default='avi')

    blogs: Mapped[list["Blog"]] = relationship("Blog", back_populates="user")

class Blog(base):
    __tablename__ = 'blogs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(length=50), index=True)
    body: Mapped[str] = mapped_column(String(length=255))
    # title02: Mapped[str] = mapped_column(String(length=200))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user_information.id'))

    user: Mapped["User"] = relationship("User", back_populates="blogs")
