from pygame import init, mixer, event
init()
mixer.music.load('ex021.mp3')
mixer.music.play()
event.wait()
