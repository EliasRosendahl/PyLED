from flask import Flask, render_template
from flask_socketio import SocketIO

from . import setLED

app = Flask(__name__)

socketio = SocketIO(app)


@app.route('/')
def index():
    print("test")
    return render_template("index.html")

@socketio.on('setLED')
def setLED(data):
    print(data)


if __name__ == "__main__":
    print("starting app")
    socketio.run(app)
