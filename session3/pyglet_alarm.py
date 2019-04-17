# import pyglet

# music = pyglet.resource.media('crowd-cheering.mp3')
# music.play()
# pyglet.app.run()

# Cach1:

from datetime import datetime
import pyglet

x = datetime.now().strftime("%H:%M")
print(x)
if x >= "20:06":
    while True:
        music = pyglet.resource.media('crowd-cheering.mp3')
        music.play()
        pyglet.app.run()
        break


# # Cach2:
# from datetime import datetime
# import pyglet
# currentTime = datetime.now().strftime("%I:%M")  
# # (I la dinh dang 12 tieng)
# alarmTime = "8:05"

# while True:
#     if currentTime >= alarmTime:
#         music = pyglet.resource.media('crowd-cheering.mp3')
#         music.play()
#         pyglet.app.run()
    
