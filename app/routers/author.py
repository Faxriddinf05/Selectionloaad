from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database.connection import get_db
from app.models.author import Author
from app.schemas.author import AddAuthor, EditAuthor

author_router = APIRouter(tags=["Author"], prefix='/author')

@author_router.get('/')
def get_author(db = Depends(get_db)):
    return db.execute(select(Author).options(selectinload(Author.books))).scalars().all()
    # or
    # result = select(Author).options(selectinload(Author.books))
    # return db.execute(result).scalars().all()

@author_router.post('/')
def add_author(data: AddAuthor, db = Depends(get_db)):
    new_author = Author(
        full_name = data.full_name,
        birth_date = data.birth_date
    )
    db.add(new_author)
    db.commit()
    return "Added"

@author_router.put('/')
def change_author(id_author: int, data: EditAuthor, db = Depends(get_db)):
    author_entity = db.execute(select(Author).where(Author.id == id_author)).scalars().first()
    author_entity.full_name = data.full_name
    author_entity.birth_date = data.birth_date
    db.commit()
    return "Edited"

@author_router.delete('/')
def remove_author(id_author: int, db = Depends(get_db)):
    author_entity = db.execute(select(Author).where(Author.id == id_author))
    db.delete(author_entity)
    db.commit()
    return "Deleted"