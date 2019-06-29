from flask import Flask
from flask import render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Vrushabh Gore',
        'title' : 'Post 1'
,        'content': 'This is the first blog'
,        'date': 'June 28,2019'
    },{
        'author': 'Rushikesh Gore'
,        'title' : 'Post 2'
,        'content': 'This is the second blog'
,        'date': 'June 28,2019'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)


@app.route("/about")
def about():
    return render_template('about.html',title = 'About US')
