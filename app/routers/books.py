from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.database.connection import get_db
from app.models.books import Book
from app.schemas.books import AddBook, EditBook

books_router = APIRouter(tags=["Books"], prefix="/books")

@books_router.get('/')
def get_books(db = Depends(get_db)):
    return db.execute(select(Book)).scalars().all()

@books_router.post('/')
def add_books(data: AddBook, db = Depends(get_db)):
    new_books = Book(
        title = data.title,
        price = data.price,
        author_id = data.author_id
    )
    db.add(new_books)
    db.commit()
    return "Added"

@books_router.put('/')
def edit_books(id_books: int, data: EditBook, db = Depends(get_db)):
    book_entity = db.execute(select(Book).where(Book.id == id_books)).scalars().first()
    book_entity.title = data.title
    book_entity.price = data.price
    book_entity.author_id = data.author_id

    db.commit()
    return "Edited"

@books_router.delete('/')
def remove(id_books: int, db = Depends(get_db)):
    book_entity = db.execute(select(Book).where(Book.id == id_books)).scalars().first()

    db.delete(book_entity)
    return "Deleted"