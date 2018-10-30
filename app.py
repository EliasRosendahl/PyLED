from flask import Flask, render_template
from flask_socketio import SocketIO

from LEDManager import LEDManager

app = Flask(__name__)
socketio = SocketIO(app)

#This is only garranteed to work if there is only 1 client
arduino = LEDManager()


@app.route('/')
def index():
    print("test")
    return render_template("index.html")

@socketio.on('setLED')
def setLED(data):
    arduino.setLED(int(data[0]), int(data[1]), int(data[2]))


if __name__ == "__main__":
    print("starting app")
    socketio.run(app)
