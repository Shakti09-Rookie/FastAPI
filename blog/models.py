from sqlalchemy import VARCHAR, ForeignKey, Integer, Column, String
from .database import Base
from sqlalchemy.orm import relationship

# sql alchemy model or model
class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    user_type = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")
