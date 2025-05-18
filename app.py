from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__) # Flask

posts = []


@app.route('/')
def index():
    if not posts:
        return render_template("index.html", posts=posts,
                          message="Henüz yazı yok")
    return render_template("index.html", posts=posts)


@app.route('/health')
def health():
    return 'OK', 200


@app.route('/post/<int:post_id>')
def post(post_id):
    try:
        return render_template("post.html", post=posts[post_id])
    except IndexError:
        return "Post not found", 404


@app.route('/new', methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        posts.append({"title": title, "content": content})
        post_id = len(posts) - 1
        return redirect(url_for("post", post_id=post_id))
    return render_template("new.html")

