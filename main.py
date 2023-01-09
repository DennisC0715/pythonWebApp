from flask import *
import requests
from post import Post
app = Flask(__name__)
url = "https://api.npoint.io/17caa9c84c420049f92b"

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



@app.route("/")
def index():
    return render_template("index.html", posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def posts(index):
    requested_post = None
    for post in data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
