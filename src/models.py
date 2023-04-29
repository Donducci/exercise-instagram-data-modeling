import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(20),nullable=False)
    phone = Column(Integer,nullable=False)
    created = Column(Integer,nullable=False)

class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    followers = Column(Integer, nullable=False)
    following = Column(Integer,nullable=False)
    updated = Column(Integer,nullable=False)

class FollowerEntry(Base):
    __tablename__ = 'follower_entry'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    followed_id = Column(Integer, ForeignKey('user.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    created = Column(String(20), nullable=False)
    updated = Column(String(20),nullable=False)
    likes = Column(Integer,nullable=False)
    comments = Column(String(250),nullable=False)

class PostComment(Base):
    __tablename__ = 'post_comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(String(250), nullable=False)
    created = Column(String(10),nullable=False)
    updated = Column(Integer,nullable=False)

class PostLikes(Base):
    __tablename__ = 'post_likes'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    likes = Column(String(1), nullable=False)
    created = Column(String(10),nullable=False)
    updated = Column(Integer,nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
