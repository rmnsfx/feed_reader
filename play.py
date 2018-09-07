import pafy
import vlc

	
if __name__ == "__main__":

	#url = "https://www.youtube.com/watch?v=TIJQlW5_CcI"
	url = "https://www.youtube.com/watch?v=LXgTp40Y3zo"
	video = pafy.new(url)
	best = video.getbest()
	playurl = best.url
	
	Instance = vlc.Instance('--no-video')
	player = Instance.media_player_new()
	Media = Instance.media_new(best.url)
	Media.get_mrl()
	player.set_media(Media)
	player.play()

	print('ok')
	
	while True:
		 pass	
