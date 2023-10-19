from mutagen.mp3 import MP3
audio = MP3("k.mp3")
print(audio.info.length/6)