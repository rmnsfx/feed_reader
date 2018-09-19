import pafy
import vlc
from flask import Flask, render_template, flash, redirect, session, url_for, request, g
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import os
import time
import datetime
from threading import Thread
from bs4 import BeautifulSoup
import urllib.request 
                        

app = Flask(__name__)
app.config['TESTING'] = False

url = [

"https://www.youtube.com/watch?v=LUOIvT9hzD8&list=RDLUOIvT9hzD8&index=1",
"https://www.youtube.com/watch?v=iQCNvkEjX9c&list=RDLUOIvT9hzD8&index=5", 
"https://www.youtube.com/watch?v=w4LkSRXrK34&list=RDLUOIvT9hzD8&index=14", 

]

videolist=[]

@app.route('/', methods=['GET', 'POST'])
def home():
    
    Instance = None   
    
    # title = None
    # duration = None
    yt_crawler()
    
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Play':            
            if Instance == None:
                Instance = vlc.Instance('--no-video')
            
                for item in videolist:
                    
                    try:
                        video = pafy.new(item)
                        best = video.getbest()
                        playurl = best.url                    

                    except:                                
                        print('Error link')
                    
                    else:
                        print(video.title, video.duration)
                        
                        player = Instance.media_player_new()
                        Media = Instance.media_new(best.url)
                        Media.get_mrl()
                        player.set_media(Media)                
                        player.audio_set_volume(100)
                        player.play()                     
                        
                        # thread = Thread(target = render_title, args = (video.title, video.duration, ))
                        # thread.daemon = True
                        # thread.start()
                        # thread.join()
                        
                        pt = datetime.datetime.strptime(video.duration,'%H:%M:%S')
                        total_seconds = pt.second+pt.minute*60+pt.hour*3600
                        
                        time.sleep(60)                             
                        # time.sleep(total_seconds - 3)                             
                        # player.audio_set_volume(50)                        
                        # time.sleep(2)                
                        player.stop()               
                    
                        #render_template('main_play.html', title = video.title, duration = video.duration)
                    
    return render_template('main_play.html') 

def yt_crawler():

    base = "https://www.youtube.com/results?search_query="
    qstring = "space+disco"
    
    data = urllib.request.urlopen(base+qstring).read()
    soup = BeautifulSoup(data)
    
    
    
    for link in soup.findAll('a', attrs={'class':'yt-uix-tile-link'}):
        #print(link['href'])
        tmp = 'https://www.youtube.com' + link['href']
        videolist.append(tmp)
        
    # for item in videolist:
        # print(item)
    
    return videolist        
        
            
    
    

    # soup = BeautifulSoup(plain_text, 'html.parser')
    
    # for link in soup.findAll('a',{'class':'yt-uix-tile-link'}):
        # lst.append('https://www.youtube.com' + link.get('href'))
        # print(lst)
    

# def render_title(title, duration):
    # return render_template('main_play.html', title = title, duration = duration)
    # print(1)

    
if __name__ == "__main__":

    app.run(debug = True)

    # home()

    # print('ok')
    
    # while True:
         # pass   
