import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(550), nullable=False)

    followers = relationship('Followers', back_populates='user')
    post = relationship('Post', back_populates='user')

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    

    user_id = Column(Integer, ForeignKey('user.id'))

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    

    followers_id = Column(Integer, ForeignKey('followers.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    

    followers_id = Column(Integer, ForeignKey('followers.id'))
    post_id = Column(Integer, ForeignKey('post.id'))





## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
