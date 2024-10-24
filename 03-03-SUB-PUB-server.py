import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    print("[INFO] The server is working on port {}".format(port))
    

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

while True:
    topic = random.randrange(9999, 10005)
    messagedata = random.randrange(1, 215) - 80
    print("[INFO] Topic {}, message {}".format(topic, messagedata))
    socket.send_string("Topic {}, message {}".format(topic, messagedata))
    time.sleep(5)