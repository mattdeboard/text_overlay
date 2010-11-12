##To Do:
##    Create "Copy URL to Clipboard" device
##    Work in Apache2/FastCGI image-serving
##    
##     
##   
##
##
##
##
##
##
##

import Image, ImageDraw, ImageFont
import sys
import random
from flask import Flask, render_template, request
from os import remove
##from flaskext.wtf import Form, TextField, validators
from wtforms import Form, TextField, validators

app = Flask(__name__)

class ImageForm(Form):
    ragetext = TextField('Enter Rage Text:', [validators.Length(min=1, max=25)])
    
@app.route('/', methods=['POST', 'GET'])
def index():
    form = ImageForm(request.form)
    if request.method == 'GET':
        return render_template('index.html', form=form)
    else:
        the_image=createimage(form.ragetext.data)
        return render_template('ragetext.html', img=the_image)

def createimage(text):
    image = Image.open("static/rageface.jpg")
    draw = ImageDraw.Draw(image)
    if len(text) <= 7:
        fontsize = 72
    else:        
        fontsize = 48
##    font = ImageFont.truetype("ARIALBD.ttf", fontsize, encoding="unic")
    font = ImageFont.truetype("static/OldSansBlack.ttf", fontsize, encoding="unic")
    draw.text((10, 10), text, font=font, fill="red")
    newname = 'images/%s.jpg' % random.randint(0,1000000000) 
    image.save(newname)
    return newname  

if __name__ == "__main__":
    app.run(debug=True)
