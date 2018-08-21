import feedparser
import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):

    def build(self):
        # return a Button() as a root widget
        #return Button(text='hello world')


        d = feedparser.parse('https://www.chitaitext.ru/rss/')

        for post in d.entries:
            post.title + " : " + post.link

        return(self)

if __name__ == '__main__':
    TestApp().run()

# d = feedparser.parse('https://www.chitaitext.ru/rss/')
#
# for post in d.entries:
#     print (post.title + " : " + post.link)

#print (d['entries'][1]['title'])
#print (d['entries'][1]['link'])