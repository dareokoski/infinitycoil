from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    posts = relationship("Post", back_populates="owner")

    @classmethod
    async def get_by_email(cls, db, email):
        return await db.execute(cls.__table__.select().where(cls.email == email)).scalar_one_or_none()

    @classmethod
    async def create(cls, db, email, hashed_password, username):
        user = cls(email=email, hashed_password=hashed_password, username=username)
        db.add(user)
        await db.commit()
        return user

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")

    @classmethod
    async def create(cls, db, owner_id, content):
        post = cls(owner_id=owner_id, content=content)
        db.add(post)
        await db.commit()
        return post

    @classmethod
    async def get_all(cls, db):
        return await db.execute(cls.__table__.select()).scalars().all()
