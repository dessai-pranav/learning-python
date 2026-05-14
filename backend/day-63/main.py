from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
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

    name: Mapped[str] = mapped_column(
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
        return f"<Book {self.name}>"

#
with app.app_context():
    db.create_all()

# with app.app_context():
#     new_book = Book( title = "New Book", author = "parth", rating = 3.14)
#     db.session.add(new_book)
#     db.session.commit()
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars().all()
#     print(all_books)
app.config['SECRET_KEY'] = 'juhyknkjnhuiskbksbxheisn'
bootstrap = Bootstrap5(app)
class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Author Name', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')


@app.route('/')
def home():
    results = db.session.execute(db.select(Book).order_by(Book.rating))
    all_books = results.scalars().all()
    return render_template("index.html", all_books=all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
            new_book = Book(
                name=form.name.data,
                author=form.author.data,
                rating=form.rating.data
            )
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('add.html',form=form)

@app.route('/edit/<int:book_id>',methods=['GET','POST'])
def edit(book_id):
    book_to_edit = db.get_or_404(Book, book_id)
    form = BookForm(
        name=book_to_edit.name,
        author=book_to_edit.author,
        rating=book_to_edit.rating
    )
    if form.validate_on_submit():
        book_to_edit.name = form.name.data
        book_to_edit.author = form.author.data
        book_to_edit.rating = form.rating.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add.html',form=form)

@app.route('/delete/<int:book_id>')
def delete(book_id):
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
