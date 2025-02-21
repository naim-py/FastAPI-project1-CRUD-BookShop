from fastapi import FastAPI
from app.database import engine, Base
from app.routes import book, user

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Bookshop API", docs_url="/docs", redoc_url="/redoc")


app.include_router(book.router, prefix="/api", tags=["Books"])
app.include_router(user.router, prefix="/api", tags=["Users"])
