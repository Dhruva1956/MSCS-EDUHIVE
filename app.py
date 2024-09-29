from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisismys3cr3tk3y"
socketio = SocketIO(app)


@app.route("/", methods=["GET", "POST"])
def index():

    return "Welcome to EDU-HIVE"

if __name__ == "__main__":
    socketio.run(app, debug=True)
