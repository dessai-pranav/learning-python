from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
post_objects = response.json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def post(index):

    requested_post = None

    for blog_post in post_objects:

        if blog_post["id"] == index:
            requested_post = blog_post
            break

    return render_template("post.html",
                           requested_post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)