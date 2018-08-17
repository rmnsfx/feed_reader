import feedparser

d = feedparser.parse('https://www.chitaitext.ru/rss/')

for post in d.entries:
    print (post.title + " : " + post.link)

#print (d['entries'][1]['title'])
#print (d['entries'][1]['link'])