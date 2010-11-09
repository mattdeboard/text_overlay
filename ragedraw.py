import Image, ImageDraw, ImageFont
import sys

from os import chdir, path

image = Image.open("static/rageface.jpg")
draw = ImageDraw.Draw(image)
 
def createimage(text, outfile):
    if len(text) <= 7:
        fontsize = 72
    else:        
        fontsize = 48
    font = ImageFont.truetype("OldSansBlack.ttf", fontsize, encoding="unic")
    draw.text((10, 10), text, font=font, fill="red")
    image.save('static/ragetext.jpg')

def returnbaseimage(self):
    image = Image.open("static/rageface.jpg")
    return image.filename
        
