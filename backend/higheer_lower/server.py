import random

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1 >Guess a number between 0 to 9</h1>"\
'<img src = https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif width="200" height="200">'
@app.route("/<number>")
def get_number(number):
    random_number = random.randint(0,9)
    if random_number > int(number):
        return '<h1 style="color: red">Its too low,Try again</h1>' \
               '<img src = https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif width="200" height="200">'
    elif random_number == int(number):
        return '<h1 style="color: green">You Found Me!</h1>' \
               '<img src = https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif width="200" height="200">'
    else:
        return '<h1> too high, try again</h1>' \
               '<img src = https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif width="200" height="200">'






