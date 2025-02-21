from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.book_service import BookService
from app import schemas

router = APIRouter()

@router.get("/books", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return BookService(db).get_books()

@router.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return BookService(db).create_book(book)

@router.put("/books/{book_id}",response_model=schemas.Book)
def update_book(book_id:int,book:schemas.BookUpdate,db:Session=Depends(get_db)):
    updated_book= BookService(db).update_book(book_id,book)
    if updated_book:
        return updated_book
    raise HTTPException(status_code=404,detail="Book not found")

@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    if BookService(db).delete_book(book_id):
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
