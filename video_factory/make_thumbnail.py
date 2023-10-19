
from PIL import Image,ImageFilter,ImageDraw,ImageFont
import arabic_reshaper
import os

im = Image.open("img.jpg")

bluerd = im.filter(ImageFilter.GaussianBlur(1.5))

todraw= ImageDraw.Draw(bluerd)
myfont= ImageFont.truetype("LMN Khordad.ttf",size=60  )



or_text = "³°w"
a= arabic_reshaper.reshape(or_text)
todraw.text((50,50),a, font=myfont,fill=(0,255,0))

bluerd.show()