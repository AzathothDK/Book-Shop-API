from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from pydantic import Optional, List

from app.models import Book
from app.schemas.book import BookCreate, BookUpdate


def create_book(db: Session, book: BookCreate) -> Book:
    db_book = Book(title=book.title, author=book.author, description=book.description)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: int) -> Optional[Book]:
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


def get_books(db: Session) -> List[Book]:
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Books not found")
    return books


def update_book(db: Session, book_id: int, book: BookUpdate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        return None
    for field, value in vars(book).items():
        setattr(db_book, field, value) if value else None
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> Optional[Book]:
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return book
    else:
        return None
