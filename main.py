# main.py
# 

# Monkey patch first
import eventlet, gevent
eventlet.monkey_patch()

from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit, disconnect

import sys, time

from subprocess import Popen, PIPE

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
proc = None

@app.route('/')
def index(): 
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def connect():
    emit('my response', {'data': 'Connected'})
    print ('client connected')

@socketio.on('disconnect', namespace='/test')
def disconnect():
    print ('Client disconnected')
    proc.kill()

@socketio.on('getcurrentface', namespace='/test')
def startrecognition():
    print ('App started')
    global proc
    proc = Popen([sys.executable, "-u", "facerec.py"], stdout=PIPE, bufsize=1)
    for line in iter(proc.stdout.readline, ''):
        emit('mode', {'data': line.rstrip()})

@socketio.on('keepalive', namespace='/test')
def keepalive(message):
    print (message['data'])
    
if __name__ == '__main__':
    app.debug = True
    socketio.run(app, host='0.0.0.0')