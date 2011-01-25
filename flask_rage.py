import Image, ImageDraw, ImageFont
import random, base64
import sys, os
from flask import Flask, render_template, request
from os import remove
from flaskext.wtf import Form, TextField, validators, Required
from imgur_upload import imgapi

app = Flask(__name__)
app.secret_key = 'b\xcaf\xde\xc3\xc6\xdc\x03\xf0ls\xd6\x08\xe7\x9a2\x02j\xdf\xa7n\xe5\xf4\xdd'

class ImageForm(Form):
    ragetext = TextField("Enter rage text:", [validators.required()])

@app.route('/', methods=("GET", "POST"))
def rage():
    try:
        form = ImageForm()
        form.ragetext.validate(form=form)
        if form.validate_on_submit():
            the_image, savefile = createimage(form.ragetext.data)
            imgpath = imgur_up(the_image)
            remove(savefile)
            return render_template('rage.html', form=form, img=imgpath)
        else:
            return render_template('rage.html', form=form)
    except Exception:
        import traceback
        print >> sys.stderr, ''.join(traceback.format_exception(*sys.exc_info()))

def createimage(text):
    image = Image.open("/a/mattdeboard.net/root/rage/static/rageface.jpg")
    draw = ImageDraw.Draw(image)
    if len(text) <= 7:
        fontsize = 72
    else:
        fontsize = 48
    font = ImageFont.truetype("/a/mattdeboard.net/root/rage/static/FreeSansBold.ttf", fontsize, encoding="unic")
    draw.text((10, 10), text, font=font, fill="red")
    fname = '%s.jpeg' % random.randint(0,1000000000)
    the_image = "images/%s" % fname
    savefile = '/a/mattdeboard.net/root/rage/images/%s' % fname
    image.save(savefile)
    return the_image, savefile

def imgur_up(img):
    f = open('/a/mattdeboard.net/root/rage/%s' % img)
    imgurl = imgapi.upload(f.read())
    print >> sys.stderr, imgurl
    try:
        return imgurl[u'rsp'][u'image'][u'original_image']
    except KeyError:
        return img


if __name__ == "__main__":
    app.run(debug=True)
