from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routes import auth, posts
from typing import AsyncGenerator

# Define lifespan context manager for startup and shutdown logic
async def lifespan(app: FastAPI) -> AsyncGenerator:
    # Code to run on startup
    await init_db()
    yield  # FastAPI will continue processing after this point
    # Code to run on shutdown (if needed, you can close database connections here)

# Initialize FastAPI app with lifespan context manager
app = FastAPI(
    title="Infinity Coil API",
    description="Backend for Infinity Coil - A Social Media Platform",
    version="1.0.0",
    lifespan=lifespan  # Pass lifespan function here
)

# Allow CORS for frontend access (adjust domains for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Infinity Coil API"}
