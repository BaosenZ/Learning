from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample blog posts data
posts = {
    1: {"title": "First Post", "content": "This is the first blog post."},
    2: {"title": "Second Post", "content": "This is the second blog post."},
    3: {"title": "Third Post", "content": "This is the third blog post."}
}

# Home route
@app.route('/')
def home():
    return render_template('home.html', posts=posts)

# Dynamic route for individual blog posts
@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = posts.get(post_id)
    if post is None:
        abort(404)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
