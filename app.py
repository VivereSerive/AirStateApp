from flask import Flask
from flask_sock import Sock

# App Initialization
app = Flask(__name__)
sock = Sock(app)

## WebSocket Route
# Reverses the String recieved from the Client
@sock.route('/reverse')
def reverse(ws):
    while True:
        text = ws.recieve()
        ws.send(text[::-1])

# ws://<your_computer_ip>:5000/echo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
# Remove debug=True when in Production

