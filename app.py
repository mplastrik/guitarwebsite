from flask import Flask, render_template
from article_data import Articles

app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

@app.route("/article/<int:id>")
def article(id):
    return render_template('article.html', article=Articles[id-1])


if __name__ == '__main__':
    app.run(debug=True)

