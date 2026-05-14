from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'juhyknkjnhuiskbksbxheisn'
all_books = []
bootstrap = Bootstrap5(app)
class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Author Name', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add",methods=['GET','POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_dict = {
            "name":form.name.data,
            "author":form.author.data,
            "rating":form.rating.data,
        }
        all_books.append(new_dict)
        print(all_books)
        return render_template("index.html", all_books=all_books)
    return render_template('add.html',form=form)


if __name__ == "__main__":
    app.run(debug=True)

