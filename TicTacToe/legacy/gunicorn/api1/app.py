from flask import Flask, render_template, request
#from flask_restful import Resource, Api
from markupsafe import escape

import pandas as pd

app = Flask(__name__, static_url_path='')

#api = Api(app)

import eventlet
import json

from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

import configparser
config = configparser.ConfigParser()
config.sections()
#config.read('app.ini')

eventlet.monkey_patch()

#app.config['SECRET'] = config['app']['SECRET']
#app.config['TEMPLATES_AUTO_RELOAD'] = config['app']['SECRET']

#username = config['web']['USERNAME']
#password = config['web']['PASSWORD']

socketio = SocketIO(app)
bootstrap = Bootstrap(app)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#api.add_resource(HelloWorld, '/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

if __name__ == '__main__':
    #app.run(debug=True)
    socketio.run(app)#, host='0.0.0.0', port=5000, use_reloader=False, debug=False)
