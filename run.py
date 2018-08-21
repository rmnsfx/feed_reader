import feedparser
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def result():
    d = feedparser.parse('https://www.chitaitext.ru/rss/')

    for post in d.entries:
        dict = post.title

                 
   
    return render_template('result.html', result = d.entries)

if __name__ == "__main__":
    app.run(debug = True)