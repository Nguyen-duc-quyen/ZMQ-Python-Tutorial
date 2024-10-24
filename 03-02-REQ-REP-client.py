import zmq
import sys

ports = ["5556"]
if len(sys.argv) > 1:
    ports[0] = sys.argv[1]

if len(sys.argv) > 2:
    ports.append(sys.argv[2])
    
# Create context
context = zmq.Context()
socket = context.socket(zmq.REQ)
for i in range(len(ports)):
    print("[INFO] Connecting to server on port {}".format(ports[i]))
    socket.connect("tcp://localhost:{}".format(ports[i]))
    

# Do 10 requests, waiting each time for a response
for request in range(1, 10):
    print("[REQ]: Sending request no {}".format(request))
    socket.send_string("[REQ]: Sending request no {}".format(request))
    
    # Get the reply
    message = socket.recv()
    print("[INFO]: received message: {}".format(message))