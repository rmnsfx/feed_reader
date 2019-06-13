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
import random
                        

app = Flask(__name__)
app.config['TESTING'] = False

name_list = []

# name_list = [
# "Flume+ezra",
# "Rawls+Errday+99",
# "Hollow+Clouds+Lopez+Theme",
# "Devotion+Uppermost",
# "Daft+Punk+Revolution+909",
# "Miike+Snow+Genghis+Khan",
# "Air+Playground+love",
# "Gorillaz+Empire+Ants",
# "Tame+Impala+The+less+I+know+the+better",
# "Tame+Impala+Let+it+happen",
# "Washed+out+Feel+it+all+around",
# "Foster+the+people+Dont+stop-remix",
# "Michael+Gray+Thee+Weekend",
# "David+Morales+Needin+U",
# "Air+La+femme+argent",
# "Tim+Deluxe+It+just+wont+do",
# "Junior+Jack+E+samba",
# "Michael+Gray+Borderline",
# "Axwell+Watch+the+sunrise",
# "C+Mos+2+Million+ways+axwell+remix",
# "Laurent+Wolf+Calinda",
# "Rui+Da+Silva+Touch+me",
# "Salome+de+bahia+Outro+lugar",
# "Basement+Jaxx+Bingo+Bango",
# ]

def get_name_list():
    
    content = []
    
    with open('content.txt') as f:
        #content = f.readlines()
        for l in f:
            content.append(l)
    
    # for item in content:
        # item = item.replace(" - "," ")
        # item = item.replace(" ","+")
        # print(item)
    
    content = [s.replace(" - "," ") for s in content]
    content = [s.replace(" ","+") for s in content]
    
    return content

@app.route('/', methods=['GET', 'POST'])
def home():
    
    name_list = get_name_list()
    
    for item in name_list:    
        print(item)
    
    if request.method == 'GET':
        return render_template('video.html') 
    
    # title = None
    # duration = None
    
    while True:              
                
        Instance = None   
        
        videolist = yt_crawler(random.choice(name_list))        
        
        
        if request.method == 'POST':                   
            
            if request.form.get('Encrypt') == 'Play':                            
                
                if Instance == None:             
                                    
                    Instance = vlc.Instance('--no-video')                   
                                    
                    for item in videolist[0:1]:
                        
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
                            
                            if total_seconds < 300:
                               time.sleep(total_seconds-5)                             
                            else:
                               time.sleep(300)                             
                            
                            
                            player.stop()               
                        
                            # render_template('main_play.html', title = video.title, duration = video.duration)
                            
                    
    return render_template('main_play.html') 

def yt_crawler(name):

    videolist = []
    
    base = "https://www.youtube.com/results?search_query="       
    qstring = name
    
    req = urllib.request.Request(base+qstring)
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)')    
    data = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data)  
    
    
    for link in soup.findAll('a', attrs={'class':'yt-uix-tile-link'})[0:1]:
        # print(link['href'])
        tmp = 'https://www.youtube.com' + link['href']
        videolist.append(tmp)
        
    # for item in videolist:
        # print(item)
    
    return videolist        
        
            


    
if __name__ == "__main__":

    app.run(debug = True)

    # home()

    # print('ok')
    
    # while True:
         # pass   
