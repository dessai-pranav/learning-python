from flask import Flask, render_template,request
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
post_objects = response.json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact", methods=["POST","GET"])
def contact():
    if request.method == "POST":
        user = os.getenv("EMAIL_USER")
        password = os.getenv("EMAIL_PASS")
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(user,password)
            message = f"""Subject: New Blog Contact Message

            Name: {data['name']}
            Email: {data['email']}
            Phone: {data['phone']}

            Message:
            {data['message']}
            """

            smtp.sendmail(
                user,
                user,
                message
            )
            return render_template("contact.html",msg_sent=True)
    return render_template("contact.html",msg_sent=False)






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