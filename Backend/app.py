from websocket import WebSocketServer, socketio, app

app = WebSocketServer().create_app()

@socketio.on('connect')
def handle_connect():
    print('Client connected.')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print(f'Received message: {message}')
    socketio.emit('message', message)


if __name__ == '__main__':
    socketio.run(app)