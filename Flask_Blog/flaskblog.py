from flask import Flask, render_template, url_for


app = Flask(__name__)


posts = [
    {
        'author': 'Onder Eren',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'November 17, 2020'
    },
    {
        'author': 'Nihan Ocak',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'November 18, 2020'
    },
]


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about_page():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)
