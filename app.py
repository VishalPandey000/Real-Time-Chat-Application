from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}  # Dictionary to store users and their rooms

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    users[username] = room
    send(f"{username} has joined the room.", room=room)

@socketio.on('message')
def handle_message(data):
    room = users.get(data['username'])
    if room:
        send(f"{data['username']}: {data['message']}", room=room)

@socketio.on('leave')
def handle_leave(data):
    username = data['username']
    room = users.get(username)
    leave_room(room)
    send(f"{username} has left the room.", room=room)
    del users[username]

if __name__ == '__main__':
    socketio.run(app, debug=True)
