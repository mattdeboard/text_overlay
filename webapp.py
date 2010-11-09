import web
from web import form
from ragedraw import RageImage

urls = ('/face', 'rageface')
render = web.template.render('templates/')

app = web.application(urls, globals())

input_form = form.Form(
    form.Textbox('Enter text:',
                 maxlength='12'
                 form.Validator("Text must be 12 characters or less", lambda x: len(x) < 13)
                 )
    form.Button('Submit')
    )

class rageface:

    def GET(self):
        rageimg = RageImage.returnbaseimage()
        return render.rageface(rageimg)

    def POST(self):
        imgname = "C:\\Documents and Settings\\mdeboard\\Desktop\\ragetext.jpg"
        form = input_form()
        if not form.validates():
            return render.formtest(form)
        else:
            RageImage.createimage(form['Enter text:'].value, imgname)
            return render.rageface(imgname)


if __name__ == "__main__": app.run()
