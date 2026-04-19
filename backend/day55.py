from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
'<p>this is  a paragraph</p>'\
'<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXkwbDd4cnF2cGplcXJudmhnZnFzaDdpdHRsNXRzNWhrdTVnMW0zMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13CoXDiaCcCoyk/giphy.gif" width=200>'

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper
def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper
def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "<h1>bye!</h1>"






# @app.route("/api/<name>")
# def hello(name):
#     return f"<p>Hello, {name}</p>"

if __name__ == "__main__":
    app.run(debug=True)