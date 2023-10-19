from moviepy.editor import AudioFileClip ,AudioClip , VideoFileClip,VideoClip,TextClip,CompositeVideoClip,ImageClip
import moviepy.video.fx.all as ffx
import re


def cnvert_audio_to_loopedvideo(audio_path:str , to_looped:VideoClip) -> VideoClip:
      # to_looped= VideoFileClip(loop_video_path)
      
      audio=AudioFileClip(audio_path)
      
      looped_clip:VideoClip=ffx.loop(to_looped,duration=audio.duration)
      looped_clip = looped_clip.set_audio(audio) 
      return looped_clip
      
      
def add_text_info(video_path:str,Genral_info:str, title:str)->VideoClip:
      font_name = "Sakkal-Majalla"
      _font_size = 50
      _font_color = "white"
      
      clip1=VideoFileClip(video_path)
      
      title = f"موضوع سخنرانی :{title}"
      title_clip:VideoClip= TextClip(title,font=font_name,fontsize=_font_size,color=_font_color )
      title_clip=title_clip.set_duration(clip1.duration)
      title_clip=title_clip.set_position(("center","top"))
      title_clip=title_clip.set_opacity(0.7)
      

      upeer_text:VideoClip=TextClip(Genral_info,font=font_name,fontsize=_font_size,color=_font_color)
      upeer_text=upeer_text.set_duration(clip1.duration)
      upeer_text=upeer_text.set_position(("center","bottom"))
      upeer_text=upeer_text.set_opacity(0.7)
      
      com=CompositeVideoClip(clips=[clip1,upeer_text,title_clip])
      return com
      
def add_pic(video:VideoClip ,img:str ,_duration:float)->VideoClip:
      
      img_clip= ImageClip(img,duration=_duration)
      img_clip=img_clip.set_opacity(0.8)
      img_clip= ffx.resize(img_clip,width=300)
      img_clip:ImageClip=img_clip.set_position((0.8,0.56),relative=True)
      com:VideoClip=CompositeVideoClip(clips=[video,img_clip])
      return com
      
      
     
def get_file_name(path:str)->str:
      _pattern =r"[^/\\]*?(?=\.\w+$)"
      
      match= re.search(_pattern,path)
      return match.group(0)
      
import mangefile
import codecs

# audio_path="resources/شش قوم برگزیده.mp3" s

audio_path =mangefile.get_unprocessed_video().strip()
vid="resources/Loop_vids/loop2.mp4"
img="resources/kafi.jpg"
genral_info ="آرشیو سخنرانی های مرحوم ایت الله احمد کافی."
duraiton=VideoFileClip(vid).duration
title = get_file_name(audio_path)


      


video_with_info=add_text_info(vid,genral_info,title)
video_whit_pic_info=add_pic(video_with_info,img,duraiton)
final_clip=cnvert_audio_to_loopedvideo(audio_path,video_whit_pic_info)
# final_clip.subclip(550,551).write_videofile("cccc.mp4",fps=25) #for test
final_clip.write_videofile(f"{title}.mp4",fps=25) #for test