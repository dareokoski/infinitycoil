from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (Modify for PostgreSQL, MySQL, or SQLite)
DATABASE_URL = "sqlite+aiosqlite:///./database.db"

# Create Async Engine & Session
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

# Dependency for database session
async def get_db():
    async with SessionLocal() as session:
        yield session

# Initialize database (for migrations)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
