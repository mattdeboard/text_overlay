import web
from web import form
from ragedraw import *

urls = ('/', 'rageface')
render = web.template.render('C:\\python27\\text2rageface\\templates\\')
imgname = "C:\\Documents and Settings\\mdeboard\\Desktop\\ragetext.jpg"

app = web.application(urls, globals())

input_form = form.Form(
    form.Textbox('input',
                 form.Validator("Text must be 12 characters or less", lambda x: len(x) < 13),
                 pre="Enter text:",
                 maxlength='12'
                 ),
    )

class rageface:

    def GET(self):
        form = input_form()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self):
        imgname = "C:\\Documents and Settings\\mdeboard\\Desktop\\ragetext.jpg"
        form = input_form()
        if not form.validates():
            return render.formtest(form)
        else:
            createimage(form['input'].value, imgname)
            return render.rageface(imgname)


if __name__ == "__main__": app.run()
