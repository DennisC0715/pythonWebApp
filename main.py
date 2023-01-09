from flask import *
import requests
from post import Post
import smtplib


app = Flask(__name__)
url = "https://api.npoint.io/17caa9c84c420049f92b"
Email_ADDRESS = "enouch0715@gmail.com"
data = requests.get(url).json()
# posts = []
#
# for item in data:
#     post = Post(item["id"], item["title"], item["subtitle"], item["author"], item["date"])
#     posts.append(post)
#     print(item)
# print(data)
#
# for items in posts:
#     print(items)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(Email_ADDRESS, "afydybevospdkvkl")
        connection.sendmail(
            from_addr=Email_ADDRESS,
            to_addrs=["chensuyuan1989@hotmail.com"],
            msg=email_message)

@app.route("/")
def index():
    return render_template("index.html", posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



@app.route("/post/<int:index>")
def posts(index):
    requested_post = None
    for post in data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#




if __name__ == "__main__":
    app.run(debug=True)
