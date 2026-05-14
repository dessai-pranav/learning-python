from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm, form
from wtforms import StringField, SubmitField,FloatField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class EditForm(FlaskForm):
    rating = FloatField('rating', validators=[DataRequired()])
    review = StringField('review', validators=[DataRequired()])
    submit = SubmitField('Submit')

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies_collection.db'

db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String,nullable=False,unique=True)
    year: Mapped[int] = mapped_column(Integer,nullable=False)
    description: Mapped[str] = mapped_column(String,nullable=False)
    rating: Mapped[float] = mapped_column(Float,nullable=False)
    ranking: Mapped[int] = mapped_column(Integer,nullable=False)
    review: Mapped[str] = mapped_column(String,nullable=False)
    img_url: Mapped[str] = mapped_column(String,nullable=False)

# with app.app_context():
#     db.create_all()
#
# new_movie = Movie(
#     title = 'Harry potter',
#     year = 2020,
#     description = 'Harry potter',
#     rating = 3.5,
#     ranking = 5,
#     review = 2,
#     img_url = "https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQBGRkjVh3ws&ved=0CBYQjRxqFwoTCPjb5_fnuJQDFQAAAAAdAAAAABAL&opi=89978449"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    movies = result.scalars().all()
    return render_template("index.html", movies=movies)

@app.route("/edit/<int:movie_id>" ,methods=["GET","POST"])
def edit(movie_id):
    movie_edit = db.get_or_404(Movie,movie_id)
    form = EditForm(
        rating = movie_edit.rating,
        review = movie_edit.review,
    )
    if form.validate_on_submit():
        movie_edit.rating = form.rating.data
        movie_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html",form=form)




if __name__ == '__main__':
    app.run(debug=True)
