import web
from web import form
from ragedraw import *
from os import path

urls = ('/', 'Index',
        '/image', 'ImageServe')
render = web.template.render('templates/')
##imgname = "static/ragetext.jpg"

app = web.application(urls, globals())

input_form = form.Form(
    form.Textbox('Enter Rage Text:',
                 form.Validator("Text must be 12 characters or less", lambda x: len(x) < 13),
                 maxlength='12'
                 ),
    )

class Index:

    def GET(self):
        form = input_form()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.index(form)

    def POST(self):
        form = input_form()
        if not form.validates():
            return render.formtest(form)
        else:
            the_image = createimage(form['Enter Rage Text:'].value)
            the_string = "hurp"
            return render.rageface(the_image, the_string)

       
    




if __name__ == "__main__": app.run()
