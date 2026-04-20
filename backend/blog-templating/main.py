from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

post_objects = []

try:
    response = requests.get(
        " https://api.npoint.io/c790b4d5cab58020d391",
        timeout=5
    )

    if response.status_code == 200:
        posts = response.json()

        if posts:
            for post in posts:
                post_obj = Post(
                    post["id"],
                    post["title"],
                    post["subtitle"],
                    post["body"]
                )
                post_objects.append(post_obj)

except Exception as e:
    print("API Error:", e)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None

    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
            break

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)