#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from flask_rage import app

WSGIServer(app).run()
