import os
import sys
import json
import traceback
import ServerUtil

from flask import Flask
from flask import jsonify
from flask import render_template

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

tfolder = os.path.join (os.path.dirname (os.path.abspath (__file__)), 'templates')
sfolder = os.path.join (os.path.dirname (os.path.abspath (__file__)), 'static')
app = Flask (__name__, template_folder=tfolder, static_folder=sfolder)

@app.route ("/")
def index ():
    return render_template ('index.html')

@app.route ("/deps/<path:path>")
def dependancies (path):
    return app.send_static_file (path)

class BainiacApp:
    def __init__ (self, bind, port):
        self.bind = bind
        self.port = port

    def listen (self):
        try:
            ServerUtil.info ('WSGIServer:[gevent] starting http://%s:%i/' \
                             % (self.bind, self.port))
            http_server = WSGIServer ((self.bind, self.port), app)
            http_server.serve_forever ()
        except KeyboardInterrupt:
            ServerUtil.warning ('Caught keyboard interupt stopping')
        except:
            ServerUtil.error ("%s" % traceback.format_exc ())
            ServerUtil.error ("%s" % sys.exc_info ()[1])
