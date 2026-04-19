
import random
from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     random_number = random.randint(1, 10)
#     current_year = datetime.now().year
#
#     return render_template("index.html",num = random_number,date = current_year)
@app.route("/guess/<name>")
def guess(name):
        response1 = requests.get(f"https://api.genderize.io?name={name}").json()
        gender = response1["gender"]
        response2 = requests.get(f"https://api.agify.io?name={name}").json()
        return render_template("index.html",name=name,gender=gender,age=response2["age"])

if __name__ == "__main__":
    app.run(debug=True)