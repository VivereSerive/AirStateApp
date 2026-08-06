from flask import Flask, render_template, jsonify
from flask_sock import Sock
from simple_websocket import ConnectionClosed

# App Initialization
app = Flask(__name__)
sock = Sock(app)

## Routes
@app.route('/')
def index():
    return render_template('index.html')

## WebSocket Route
# ESP
@sock.route('/ws')
def wsESP32(ws):
    while True:
        try:
            # Wait 1 second for message
            message = ws.recieve(timeout=1)
        except ConnectionClosed:
            break

# Reverses the String recieved from the Client
@sock.route('/reverse')
def reverse(ws):
    while True:
        text = ws.receive()
        if text is None:
            break
        ws.send(text[::-1])

# ws://<your_computer_ip>:5000/reverse
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
# Remove debug=True when in Production