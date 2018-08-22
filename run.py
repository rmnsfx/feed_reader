import feedparser
from flask import Flask, render_template
app = Flask(__name__)
all = {
    'https://www.chitaitext.ru/rss/': '/chitaitext',
}



@app.route('/')
def result():    
  
    return render_template('main.html', all = all)
    
@app.route('/chitaitext')
def result_1():    
   
    url = 'https://www.chitaitext.ru/rss/'
    d = feedparser.parse(url)
  
    return render_template('result.html', result = d.entries, url = url)   
    



if __name__ == "__main__":
    app.run(debug = True)