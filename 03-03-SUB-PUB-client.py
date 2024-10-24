import sys
import zmq

ports = ["5556"]
if len(sys.argv) > 1:
    ports[0] = sys.argv[1]

if len(sys.argv) > 2:
    ports.append(sys.argv[2])
    
context = zmq.Context()
socket = context.socket(zmq.SUB)
for i in range(len(ports)):
    print("[INFO] Connecting to server on port {}".format(ports[i]))
    socket.connect("tcp://localhost:{}".format(ports[i]))
    

# Client usually set a filter on these topic of their interests
# In this case, the messages are filtered using zip code (10001 - NYC)
topic_filter = "Topic 10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

# Process 5 updates
total_value = 0
for update_nbr in range(5):
    message = socket.recv()
    data = message.split()
    topic = data[1]
    message_data = data[3]
    print("[INFO] Topic {}, message {}".format(data, message_data))
