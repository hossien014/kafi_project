from moviepy.editor import TextClip,VideoClip,ColorClip,VideoFileClip,CompositeVideoClip,AudioFileClip
from mutagen.mp3 import MP3

audio_address= "k.mp3"
length = MP3(audio_address).info.length
audio_clip= AudioFileClip(audio_address)
clip1 = ColorClip(size=(200,200),color=[0,0,50],duration=length,ismask=False )
# text = TextClip (txt="سخرانی ایت الله کافی ",size=(500,100),bg_color="red",color="blue",stroke_color= "black", stroke_width=2,kerning=2,method="caption")
# text = text.set_duration(3)
# text= text.set_position("center")

clip1.set_audio(audio_clip)
clip1.write_videofile("vs.mp4" , fps = 20)
# res = CompositeVideoClip(clips=[clip1,text])
# res.set_audio(audio_clip)
# res.write_videofile("ts.mp4" ,fps=25)





