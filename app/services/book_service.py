from sqlalchemy.orm import Session
from app import models, schemas

class BookService:
    def __init__(self, db: Session):
        self.db = db

    def get_books(self):
        return self.db.query(models.Book).all()

    def get_book_by_id(self, book_id: int):
        return self.db.query(models.Book).filter(models.Book.id == book_id).first()

    def create_book(self, book_data: schemas.BookCreate):
        new_book = models.Book(**book_data.dict())
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        return new_book

    def update_book(self,book_id:int,book_data:schemas.BookUpdate):
        book =self.get_book_by_id(book_id)
        if not book:
            return None
        for key,value in book_data.dict(exclude_unset=True).items():
            setattr(book,key,value)
        self.db.commit()
        self.db.refresh(book)
        return book

    def delete_book(self, book_id: int):
        book = self.db.query(models.Book).filter(models.Book.id == book_id).first()
        if book:
            self.db.delete(book)
            self.db.commit()
            return True
        return False
