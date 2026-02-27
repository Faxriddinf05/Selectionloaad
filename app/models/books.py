from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base
# from app.models.author import Author


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    price: Mapped[int]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))

    author: Mapped["Author"] = relationship(back_populates="books")