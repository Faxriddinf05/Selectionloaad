import datetime

from pydantic import BaseModel

class AddAuthor(BaseModel):
    full_name: str
    birth_date: datetime.date

class EditAuthor(AddAuthor):
    pass