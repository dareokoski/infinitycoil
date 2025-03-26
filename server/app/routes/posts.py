from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Post
from app.schemas import PostCreate, PostResponse
from app.security import get_current_user

router = APIRouter()

@router.post("/", response_model=PostResponse)
async def create_post(post_data: PostCreate, user=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    new_post = await Post.create(db, user.id, post_data.content)
    return new_post

@router.get("/", response_model=list[PostResponse])
async def get_posts(db: AsyncSession = Depends(get_db)):
    return await Post.get_all(db)
