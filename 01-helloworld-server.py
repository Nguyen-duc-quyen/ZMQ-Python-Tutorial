import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


while True:
    message = socket.recv()
    print(f"Received request: {message}")

    # Do some work
    time.sleep(1)

    # Send reply back to client
    socket.send(b"World")