from flask import Flask, render_template
from flask_socketio import SocketIO
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('setLED')
def setLED(data):
    pass


if __name__ == "__main__":
    print("starting app")
    app.run()
