import Image, ImageDraw, ImageFont
import sys
from os import chdir, path

class RageImage:
    
    image = Image.open("C:\\Documents and Settings\\mdeboard\\Desktop\\rageface.jpg")
    draw = ImageDraw.Draw(image)

    def textformat():
        overlay_text = raw_input("Enter rage text (max=12 chars, incl spaces):")[0:12]
        

        return overlay_text, font

    @classmethod
    def createimage(text, outfile):
        if len(text) <= 7:
            fontsize = 72
        else:        
            fontsize = 48
        font = ImageFont.truetype("ARIALBD.TTF", fontsize, encoding="unic")
        draw.text((10, 10), text, font=font, fill="red")
        image.save(outfile)

    @classmethod
    def returnbaseimage():
        return image.filename
        
