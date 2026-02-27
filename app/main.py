from fastapi import FastAPI
from app.routers.author import author_router
from app.routers.books import books_router
from app.models.books import Book


app = FastAPI(title="Selectionload", docs_url='/')

app.include_router(author_router)
app.include_router(books_router)