from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields import StringField
import secrets
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/login" ,methods = ['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        return render_template('success.html')
    return render_template('login.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)
