import datetime
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base
# from app.models.books import Book


class Author(Base):
    __tablename__ = "author"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name:Mapped[str]
    birth_date:Mapped[datetime.date]

    books: Mapped[List["Book"]] = relationship(back_populates="author")