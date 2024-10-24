import zmq
import time
import sys
import argparse


port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    print("[INFO] The current server is working on port {}".format(port))
    

# Initilize context
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)


while True:
    # Wait for request from client
    message = socket.recv()
    print("[INFO] Received request: {}".format(message))
    time.sleep(10)
    
    # Sending reply
    socket.send_string("[INFO] This is a reply from {}".format(port))