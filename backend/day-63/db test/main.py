# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title VARCHAR(250) NOT NULL UNIQUE, author VARCHAR(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES (1, 'HARRY POTTER', 'J.K.ROWLINGS', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer,String,Float



class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_collection.db'

db.init_app(app)


class Book(db.Model):

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    title: Mapped[str] = mapped_column(
        String(250),
        unique=True,
        nullable=False
    )

    author: Mapped[str] = mapped_column(
        String(250),
        nullable=False
    )

    rating: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    def __repr__(self):
        return f"<Book {self.title}>"


# with app.app_context():
#     db.create_all()
#
# with app.app_context():
#     new_book = Book( title = "New Book", author = "parth", rating = 3.14)
#     db.session.add(new_book)
#     db.session.commit()

with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    print(all_books)