from pydantic import BaseModel

class AddBook(BaseModel):
    title: str
    price: int
    author_id: int

class EditBook(AddBook):
    pass