import Image, ImageDraw, ImageFont
import sys
import random
from os import remove

def createimage(text):
    image = Image.open("static/rageface.jpg")
    draw = ImageDraw.Draw(image)
    if len(text) <= 7:
        fontsize = 72
    else:        
        fontsize = 48
    font = ImageFont.truetype("ARIALBD.ttf", fontsize, encoding="unic")
##    font = ImageFont.truetype("OldSansBlack.ttf", fontsize, encoding="unic")
    draw.text((10, 10), text, font=font, fill="red")
    newname = 'static/%s.jpg' % random.randint(0,1000000000) 
    image.save(newname)
    print newname
    return newname   
