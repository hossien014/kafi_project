from moviepy.editor import VideoFileClip,AudioFileClip ,ipython_display,ColorClip ,TextClip, ImageClip,CompositeVideoClip
# import moviepy.video.fx.all as vfx
import moviepy.video.fx.all  as a

# audio= AudioFileClip("k.mp3")
# length =audio.duration
# imgclip =ImageClip("img.jpg",duration=length)

loop_file = VideoFileClip("looped.mp4")

clip = a.loop(loop_file,duration=50)

clip.write_videofile("ll.mp4",fps=25)


# txt="ارشیو سخنرانی های ایت الله کافی. وفات 1357 هجری"
# font_name = "Sakkal-Majalla"
# text=TextClip(txt,font=font_name,fontsize=20 , stroke_color="white")
# text=text.set_duration(10)
# text=text.set_position((30,30))
# text=text.set_position(("center","bottom"))

# videoclip= imgclip.set_audio(audio)

# res= CompositeVideoClip(clips=[videoclip,text]).subclip(0,10)

# res.write_videofile("m.mp4",fps=20)



      
      
